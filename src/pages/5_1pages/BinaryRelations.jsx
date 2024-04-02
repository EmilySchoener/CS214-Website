// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const BinaryRelations = () => {

    const [S, setS] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            alert (`S List: ${S}`);
            const response = await axios.post("http://127.0.0.1:5000/submitBinary", {
                S,
            });
            console.log("Response from server:", response.data);
        } catch (error) {
            console.error("Error:", error);
        }
        window.location.reload();
    }

     const sChange= (e) => {
        setS(e.target.value);
    }

    useEffect(() => {
    // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitBinary")
      .then(response => {
        // Update the state with the response data
        setResponseData(response.data);
        console.log(responseData);
      })
      .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
  }, []);

       console.log(responseData);
    return (
        <div>
            <h1>
                5.1 - Binary Relations webpage.
            </h1>
            <Splitter>
                <SplitterPanel>
            <p> Input: </p>
            <form onSubmit={handleSubmit}>
                <input

                    onChange={sChange}
                    placeholder="Enter the pairs in S"
                />
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>
        <h2>Solution</h2>
            <h2>Response from Flask Backend</h2>
            {responseData !== null && Array.isArray(responseData) ? (
                <ul>
                    {responseData.map((item, index) => (
                        <li key={index}>{item}</li>
                    ))}
                </ul>
            ) : (
                <p> ... Loading ...</p>
            )}
                </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>Input: [[1,2],[3,4],[5,6]] </p>
                    <p>The list of S is not reflexive <br/>
                        The list of S is irreflexive<br/>
                        The list of S is not symmetric<br/>
                        The list of S is not antisymmetric<br/>
                        The list of S is not transitive</p>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default BinaryRelations