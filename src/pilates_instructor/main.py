#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from pilates_instructor.crew import PilatesInstructor

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with default inputs for a full-body 60-minute session
    """
    inputs = {
        "session_focus": "full body",
        "session_duration_minutes": 60,
        "student_feedback": "",         # Optional: prior session feedback
        "contraindications": "",  
    }
    try:
        PilatesInstructor().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    Usage: train <n_iterations> <output_filename>
    """
    inputs = {
        "session_focus": "full body",
        "session_duration_minutes": 60,
        "student_feedback": "",
        "contraindications": "",
    }
    try:
        PilatesInstructor().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    Usage: replay <task_id>
    """
    try:
        PilatesInstructor().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return results.
    Usage: test <n_iterations> <eval_llm>
    """
    inputs = {
        "session_focus": "full body",
        "session_duration_minutes": 60,
        "student_feedback": "",
        "contraindications": "",
    }
    try:
        PilatesInstructor().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with a trigger payload (for scheduled/external triggers).
    Usage: run_with_trigger '<json_payload>'

    Expected payload keys (all optional):
        session_focus          (str)  e.g. "full body", "upper body"
        session_duration_minutes (int) default 60
        student_feedback       (str)  feedback from a prior session
        contraindications      (str)  e.g. "spondylolysis, lower back pain"
    """
    if len(sys.argv) < 2:
        raise Exception(
            "No trigger payload provided. Please pass a JSON string as the first argument."
        )

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError as exc:
        raise Exception(f"Invalid JSON payload: {exc}")

    inputs = {
        "crewai_trigger_payload":       trigger_payload,
        "session_focus":                trigger_payload.get("session_focus", "full body"),
        "session_duration_minutes":     trigger_payload.get("session_duration_minutes", 60),
        "student_feedback":             trigger_payload.get("student_feedback", ""),
        "contraindications":            trigger_payload.get("contraindications", ""),
    }

    try:
        result = PilatesInstructor().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")