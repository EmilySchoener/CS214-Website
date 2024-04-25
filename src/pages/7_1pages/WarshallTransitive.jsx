import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const WarshallTransitive = () => {
    const [set, setSet] = useState([]);
    const [p, setP] = useState([]);
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/7_1_5", {
                set,
                p,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const setChange= (e) => {
        setSet(e.target.value);
    }
    const pChange= (e) => {
        setP(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/7_1_5")
      .then(response => {
        // Update the state with the response data
        setResponseData(response.data);
      })
      .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
    }

    useEffect(() => fetchData(), []);

    return (
        <div>
            <h1>
                Chapter 7.1 - Warshall Algo to Transitive Closure
            </h1>
            <form onSubmit={handleSubmit}>
                <label>Please enter your set with a comma separating each element.
                    <input
                        onChange={setChange}
                        type="text"
                        value={set}
                        placeholder="Enter Set Here"
                    />
                </label>
                <br/><br/>
                <label>Please enter your p with parentheses around each point and a comma between points. <br/> p =
                    <input
                        onChange={pChange}
                        type="text"
                        value={p}
                        placeholder="Enter Ordered Pairs Here"
                    />

                </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>

            <h2>Solution</h2>
            {responseData !== null ? (
                <pre>{responseData}</pre>
            ) : (
                <p>Loading...</p>
            )}

        </div>
    );
};

export default WarshallTransitive