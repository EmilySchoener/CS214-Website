import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const TrueOrFalse = () => {
    const [condition, setCondition] = useState("1");
    const [set1, setSet1] = useState([]);
    const [set2, setSet2] = useState([]);
    const [set3, setSet3] = useState([]);
    const [leftSide, setLeftSide] = useState([]);
    const [rightSide, setRightSide] = useState([]);
    const [responseData, setResponseData] = useState(null);

    //When user presses the submit button.
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/4_1_1", {
                condition,
                set1,
                set2,
                set3,
                leftSide,
                rightSide,
            });
            console.log("Response from server:", response.data);
        } catch (error) {
            console.error("Error:", error);
        }
        window.location.reload();
    }

    //For input changes
    const conditionChange= (e) => {
        setCondition(e.target.value);
    }
    const set1Change= (e) => {
        setSet1(e.target.value);
    }
    const set2Change= (e) => {
        setSet2(e.target.value);
    }
    const set3Change= (e) => {
        setSet3(e.target.value);
    }
    const leftSideChange= (e) => {
        setLeftSide(e.target.value);
    }
    const rightSideChange= (e) => {
        setRightSide(e.target.value);
    }

    useEffect(() => {
        // Make an HTTP GET request to your Flask backend
        axios.get("http://localhost:5000/4_1_1")
          .then(response => {
            // Update the state with the response data
            setResponseData(response.data);
          })
          .catch(error => {
            // Handle any errors
            console.error('Error fetching data:', error);
          });
      }, []);

    return (
        <div>
            <h1>
                4.1 - True or False Webpage.
            </h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Set 1 =
                    <input
                        onChange={set1Change}
                        type="text"
                        value={set1}
                        placeholder="Enter Base Case Here"
                    />
                </label>
                <br/>
                <label>
                    Set 2 =
                    <input
                        onChange={set2Change}
                        type="text"
                        value={set2}
                        placeholder="Enter Base Case Here"
                    />
                </label>
                <br/>
                <label>
                    Set 3 =
                    <input
                        onChange={set3Change}
                        type="text"
                        value={set3}
                        placeholder="Enter Base Case Here"
                    />
                </label>
                <br/>
                <label>
                    Please enter in the conditions. To use sets: use set1, set2, and set3.
                    <input
                        onChange={leftSideChange}
                        type="text"
                        value={leftSide}
                        placeholder="Enter left side of condition here"
                    />
                </label>
                <select id="dropdown" value={condition} onChange={conditionChange}>
                    <option value="1">Element of (∈)</option>
                    <option value="2">Proper subset (⊂)</option>
                    <option value="3">Subset (⊆)</option>
                </select>
                <label>
                    <input
                        onChange={rightSideChange}
                        type="text"
                        value={rightSide}
                        placeholder="Enter right side of condition here"
                    />
                </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>

            <h2>Solution</h2>
            <h2>Response from Flask Backend</h2>
            {responseData !== null ? (
                <p> {responseData} </p>
            ) : (
                <p> ... Loading ...</p>
            )}
        </div>
    );
};

export default TrueOrFalse;
