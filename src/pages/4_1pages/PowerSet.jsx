import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const PowerSet = () => {
    const [s, setS] = useState("");
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:5000/4_1_2", {
                s: s.split(",").map(item => item.trim()) // Splitting input string into an array
            });
            setResponseData(response.data); // Update response data
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const sChange= (e) => {
        setS(e.target.value);
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
            <form onSubmit={handleSubmit}>
                This will find ℘(S) for your S. Please enter each element separated by a comma.
                <br/>
                <label>
                    S =
                    <input
                        onChange={sChange}
                        type="text"
                        value={s}
                        placeholder="Enter Set Here"
                    />
                </label>
                <br/>
                <button type="submit">Submit</button>
            </form>

            <h2>Solution</h2>
            <h2>Response from Flask Backend</h2>
            {responseData !== null ? (
                <p> ℘(S) = {responseData}</p>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default PowerSet;