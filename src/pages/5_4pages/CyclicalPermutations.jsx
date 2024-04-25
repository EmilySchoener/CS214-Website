// Filename - pages/5_4pages/CyclicalPermutations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const CyclicalPermutations = () => {

    const [S, setS] = useState("");
    const [set, setInitial] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
           // alert (`S List: ${S}`);
            const response = await axios.post("http://127.0.0.1:5000/submitCyclical", {
                S,
                set,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }

    }

     const sChange= (e) => {
        setS(e.target.value);
    }

    const setChange= (e) => {
        setInitial(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitCyclical")
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
                5.4 - Cyclical Permutations webpage.
            </h1>
            <Splitter>
                <SplitterPanel>
            <p> Input: </p>
            <form onSubmit={handleSubmit}>
                <label> Type in the Initial Set S:
                    <input

                        onChange={setChange}
                        placeholder="Enter the initial set"
                    />
                </label>
                <br/>
                <label> Type in the Pairs of the relation:
                    <input

                        onChange={sChange}
                        placeholder="Enter the pairs in the relation"
                    />
                </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>
            <h2>Solution</h2>
            {responseData}
                    </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>Type in the Initial Set: [1, 2, 3, 4] </p>
                    <p>Type in the pairs of the relation: [[1, 2], [2, 3], [3, 4], [4, 1]]  </p>
                    <p>Output: 1234 <br/>
                        </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );


};

export default CyclicalPermutations