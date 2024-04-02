// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";


const MatrixMultiplication = () => {

    const [matrix1, setMatrix1] = useState("");
    const [matrix2, setMatrix2] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            alert (`First Matrix: ${matrix1}, Second Matrix: ${matrix2}`);
            const response = await axios.post("http://127.0.0.1:5000/submitMatrixMult", {
                matrix1,
                matrix2,
            });
            console.log("Response from server:", response.data);
        } catch (error) {
            console.error("Error:", error);
        }
        window.location.reload();
    }

    const Matrix1Change= (e) => {
        setMatrix1(e.target.value);
    }

     const Matrix2Change= (e) => {
        setMatrix2(e.target.value);
    }


    useEffect(() => {
    // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitMatrixMult")
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
                5.7 - Matrix Multiplication webpage.
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

export default MatrixMultiplication