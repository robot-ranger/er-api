import logging
import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum
import uvicorn

app = FastAPI(title="Enabled Robotics REST Interface Simulator")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Define enums for state values
class RobotState(str, Enum):
	IDLE = "Idle"
	EMERGENCY_STOP = "Emergency Stop Active"
	SAFEGUARD_STOP = "Safeguard Stop Active"
	ENTITY_ERROR = "Entity Error Active"
	NO_PROGRAM = "No Program"
	LOADING_PROGRAM = "Loading Program"
	READY = "Ready"
	RECOVERY = "Recovery"
	EXECUTING = "Executing"
	PAUSING = "Pausing Execution"
	PAUSED = "Paused"
	STOPPING = "Stopping Execution"
	EXECUTION_ERROR = "Execution Error Active"
	JOYSTICK_ACTIVE = "Joystick Active"

class ProgramSettingType(int, Enum):
	TYPE_0 = 0
	TYPE_1 = 1
	TYPE_2 = 2
	TYPE_3 = 3
	TYPE_4 = 4
	TYPE_5 = 5
	TYPE_6 = 6
	TYPE_7 = 7
	TYPE_8 = 8

# Define Pydantic models for the schemas
class ProgramSetting(BaseModel):
	name: str
	type: ProgramSettingType
	value: str

class WebhookInfo(BaseModel):
	uri: str
	context: Optional[str] = None

class Program(BaseModel):
	name: str
	arguments: Optional[List[ProgramSetting]] = []
	webhook: Optional[WebhookInfo] = None

class State(BaseModel):
	state: RobotState

class StateChange(BaseModel):
	state: str
	
	class Config:
		schema_extra = {
			"example": {
				"state": "Executing"
			}
		}

class Status(BaseModel):
	state: RobotState
	current_program: Optional[Program] = None
	battery: Optional[int] = None
	message: Optional[str] = None

# In-memory robot state
robot_status = Status(
	state=RobotState.IDLE,
	battery=67,
	current_program=None,
	message=None
)

@app.get("/v2/status", response_model=Status, tags=["Status"])
async def get_status():
	"""Get the current status of the robot"""
	status = robot_status
	status.battery = random.randint(0, 100)  # Simulate battery level change
	logging.info(f"Current battery level: {status.battery}%")
	return robot_status

@app.put("/v2/status", response_model=Status, tags=["Status"])
async def update_status(state_change: StateChange):
	"""Change the state of the robot"""
	# Validate state change
	allowed_states = ["Executing", "Paused", "Ready"]
	if state_change.state not in allowed_states:
		raise HTTPException(
			status_code=400,
			detail=f"Invalid state change. Allowed states: {', '.join(allowed_states)}"
		)
	
	# Update robot state
	robot_status.state = state_change.state
	
	# If switching to executing but no program is loaded
	if state_change.state == "Executing" and robot_status.current_program is None:
		robot_status.state = RobotState.EXECUTION_ERROR
		robot_status.message = "Cannot execute: No program loaded"
	
	return robot_status

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)