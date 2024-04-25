import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';

const PowerSet = () => {
    const [set, setSet] = useState("1,2,3");
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:5000/4_1_2", {
                set
            });
            setResponseData(response.data); // Update response data
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const setChange= (e) => {
        setSet(e.target.value);
    }

    useEffect(() => {
        // Make an HTTP GET request to your Flask backend when the component mounts
        axios.get("http://127.0.0.1:5000/4_1_2")
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
            <h1>4.1 - Power Set Webpage.</h1>
            <Splitter>
                <SplitterPanel>
            <form onSubmit={handleSubmit}>
                This will find ℘(S) for your S. Please enter each element separated by a comma.
                <br/>
                <label>
                    S =
                    <input
                        onChange={setChange}
                        type="text"
                        value={set}
                        placeholder="Enter Set Here"
                    />
                </label>
                <br/>
                <button type="submit">Submit</button>
            </form>

            <h2>Solution</h2>
            {responseData !== null ? (
                <p> ℘(S) = {responseData}</p>
            ) : (
                <p>Loading...</p>
            )}
                </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>
                        S = 1,2,3 <br/>
                    </p>
                    <p>
                        Solution: <br/>
                        {'℘(S) = {{∅}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}}'}
                    </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default PowerSet;