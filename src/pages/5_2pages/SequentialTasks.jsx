// Filename - pages/5_2pages/SequentialTasks.jsx
import React, {useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';

const SequentialTasks = () => {
    const [tasks, setTasks] = useState([]);
    const [task_Input, set_Task_Input] = useState("");
    const [tasks_Ordered, set_Tasks_Ordered] = useState([]);
    const handleInputChange = (e) => {
        set_Task_Input(e.target.value);
    }

    //When user presses the submit button.
    const handleSubmit = (e) => {
        if(task_Input.trim() !== ""){
            setTasks([...tasks, task_Input]);
            set_Task_Input("")
        }
    }

    const handleTaskSubmission = async () =>{
        try{
            console.log("Sending tasks:", tasks);
            const response = await axios.post("http://localhost:5000/submitTasks", {
                tasks: tasks,
            });
            set_Tasks_Ordered(response.data["Ordered Tasks"]);
        } catch(error){
            console.error("Error", error);
        }
    };

    return (
        <div>
            <h1>
                5.2 - Sequential Tasks webpage.
            </h1>
            <Splitter>
                <SplitterPanel>
            <p> Input Your Tasks: </p>
            <p>Note: The format of typing in a task is as follows: Toss Salad, Prerequisite Tasks are Tasks 2 and 3 or
                Chop Onions, Prerequisite Task is Task 9 or Cut up Chicken, no prerequisite</p>
            <p>After you type in a task, press Add Task and once you have added all your tasks, press Send Tasks to get them ordered</p>
            <input
                type="text"
                value={task_Input}
                onChange={handleInputChange}
                placeholder="Enter a task"
                size="50"
            />
            <br/>
            <button onClick={handleSubmit}>Add Task</button>
            <button onClick={handleTaskSubmission}>Send Tasks</button>

            <p> Tasks Entered: </p>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>{task}</li>
                ))}
            </ul>
            <p>Ordered Tasks:</p>
            <ul>
                {tasks_Ordered.map((task, index) => (
                    <li key={index}>{task}</li>
                ))}
            </ul>
                    </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>Tasks Entered:<br/>
                        Chop Onions, Prerequisite Task is Task 9<br/>
                        Wash Lettuce, Prerequisite Task is Task 11<br/>
                        Make Dressing, Prerequisite Task is Task 11<br/>
                        Do Stir Fry, Prerequisite Task is Task 10<br/>
                        Toss Salad, Prerequisite Tasks are Tasks 2 and 3<br/>
                        Cut up Chicken, no prerequisite<br/>
                        Grate Ginger, Prerequisite Task is Task 9<br/>
                        Chop Bok Choy, Prerequisite Task is Task 9<br/>
                        Marinate Chicken, Prerequisite is task 6<br/>
                        Heat Wok, Prerequisite tasks are tasks 1, 7, 8, and 11<br/>
                        Prepare Rice, no prerequisite<br/></p>
                    <p>Ordered Tasks:<br/>
                        Cut up Chicken, no prerequisite <br/>
                        Marinate Chicken<br/>
                        Chop Onions<br/>
                        Grate Ginger<br/>
                        Chop Bok Choy<br/>
                        Prepare Rice, no prerequisite<br/>
                        Wash Lettuce<br/>
                        Make Dressing<br/>
                        Toss Salad<br/>
                        Heat Wok<br/>
                        Do Stir Fry<br/></p>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default SequentialTasks;