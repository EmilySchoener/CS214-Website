// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";


const BooleanMatrices = () => {

    const [bool_matrix1, setMatrix1] = useState("");
    const [bool_matrix2, setMatrix2] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            alert (`First Matrix: ${bool_matrix1}, Second Matrix: ${bool_matrix2}`);
            const response = await axios.post("http://127.0.0.1:5000/submitBoolMatrix", {
                bool_matrix1,
                bool_matrix2,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }

    }

    const Matrix1Change= (e) => {
        setMatrix1(e.target.value);
    }

     const Matrix2Change= (e) => {
        setMatrix2(e.target.value);
    }


    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitBoolMatrix")
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

       console.log(responseData);
    return (
        <div>
            <h1>
                5.7 - Boolean Matrix webpage.
            </h1>
            <p> Input: </p>
            <form onSubmit={handleSubmit}>
                <input
                    onChange={Matrix1Change}
                    placeholder="Enter the first matrix"
                />
                <br/>
                <input
                    onChange={Matrix2Change}
                    placeholder="Enter the second matrix"
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
        </div>
    );


};

export default BooleanMatrices