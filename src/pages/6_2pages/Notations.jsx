import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';

const Notations = () => {
    const [notation, setNotation] = useState("1");
    const [input, setInput] = useState([]);
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/6_2_5", {
                notation,
                input,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const notationChange= (e) => {
        setNotation(e.target.value);
    }
    const inputChange= (e) => {
        setInput(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/6_2_5")
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
                Chapter 6.2 - Prefix, Postfix, and Infix Notations
            </h1>
            <form onSubmit={handleSubmit}>
                Which notation are you entering?
                <select id="dropdown" value={notation} onChange={notationChange}>
                    <option value="1">Prefix</option>
                    <option value="2">Infix</option>
                    <option value="3">Postfix</option>
                </select>
                <br/>
                <label>Please enter your expression in the format you selected.
                    <input
                        onChange={inputChange}
                        type="text"
                        value={input}
                        placeholder="Enter Here"
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
                <pre> {responseData} </pre>
            ) : (
                <p> ... Loading ...</p>
            )}

        </div>
    );
};

export default Notations
