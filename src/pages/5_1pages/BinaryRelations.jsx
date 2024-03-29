// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";


const BinaryRelations = () => {

    const [S, setS] = useState("1");
    const [responseData, setResponseData] = useState(null);

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
      })
      .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
  }, []);

    return (
        <div>
            <h1>
                5.1 - Binary Relations webpage.
            </h1>
            <p> Input: </p>
            <form onSubmit={handleSubmit}>
                <textarea
                    rows={5}
                    cols={35}
                    onChange={sChange}
                    placeholder="Enter the pairs in S"
                />
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>
           <h2>
            Solution
            </h2>
            <h2>Response from Flask Backend</h2>
            {responseData ? <ul>{responseData.map(item => <p>{item}</p>)} </ul> : <p>Loading...</p>}
        </div>
    );
};

export default BinaryRelations