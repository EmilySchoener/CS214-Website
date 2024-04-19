// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const BinaryRelations = () => {

    const [part1, setPart1] = useState("");
    const [part2, setPart2] = useState("");
    const [set, setInitial] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
           // alert (`Partition 1 ${part1}, Partition 2: ${part2} Set: ${set}`,);
            const response = await axios.post("http://127.0.0.1:5000/submitEquivalence", {
                part1,
                part2,
                set,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }

    }

     const part1Change= (e) => {
        setPart1(e.target.value);
    }

     const part2Change= (e) => {
        setPart2(e.target.value);
    }

      const setChange= (e) => {
        setInitial(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitEquivalence")
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
                5.1 - Equivalence Relations webpage.
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
                <label> Enter the first partition:
                <input
                    onChange={part1Change}
                    placeholder="Enter the set of the first partition"
                />
                    </label>
                <br/>
                <label> Enter the second partition:
                <input
                    onChange={part2Change}
                    placeholder="Enter the set of the second partition"
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
                    <p>Type in the Initial Set S: [1,2,3,4,5,6] </p>
                    <p>Enter the first partition: [1,2,3,4] </p>
                    <p>Enter the second partition: [5,6] </p>
                    <p>The Equivalence Relation is: [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3,
                        1], [3, 2], <br/>
                        [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4], [5, 5], [5, 6], [6, 5], [6, 6]]
                    </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );


};

export default BinaryRelations