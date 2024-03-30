// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";


const BinaryRelations = () => {

    const [part1, setPart1] = useState("");
    const [part2, setPart2] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            alert (`Partition 1 ${part1}, Partition 2: ${part2}`);
            const response = await axios.post("http://127.0.0.1:5000/submitEquivalence", {
                part1,
                part2,
            });
            console.log("Response from server:", response.data);
        } catch (error) {
            console.error("Error:", error);
        }
        window.location.reload();
    }

     const part1Change= (e) => {
        setPart1(e.target.value);
    }

     const part2Change= (e) => {
        setPart2(e.target.value);
    }

    useEffect(() => {
    // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitEquivalence")
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
                5.1 - Equivalence Relations webpage.
            </h1>
            <p> Input: </p>
            <form onSubmit={handleSubmit}>
                <input
                    onChange={part1Change}
                    placeholder="Enter the set of the first partition"
                />
                <br/>
                <input
                    onChange={part2Change}
                    placeholder="Enter the set of the second partition"
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

export default BinaryRelations