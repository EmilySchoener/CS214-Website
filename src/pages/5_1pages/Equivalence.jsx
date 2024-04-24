// Filename - pages/5_1pages/Equivalence.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const Equivalence = () => {

    const [part1, setPart1] = useState("");
    const [part2, setPart2] = useState("");
    const [part3, setPart3] = useState("");
    const [set, setInitial] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const part1Array = part1.match(/\w+/g);
            const part2Array = part2.match(/\w+/g);
            const part3Array = part3.match(/\w+/g);
            const setArray = set.match(/\w+/g);
            e.preventDefault(); //This will stop the handler from emptying the text box.
           // alert (`Partition 1 ${part1}, Partition 2: ${part2} Set: ${set}`,);
            const response = await axios.post("http://127.0.0.1:5000/submitEquivalence", {
                part1: part1Array,
                part2: part2Array,
                part3: part3Array,
                set: setArray,
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

    const part3Change= (e) => {
        setPart3(e.target.value);
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
                        <label> Enter the third partition:
                            <input
                                onChange={part3Change}
                                placeholder="Enter the set of the third partition"
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
                    <p>Type in the Initial Set S: [a,b,c,d,e] </p>
                    <p>Enter the first partition: [a,b,c] </p>
                    <p>Enter the second partition: [d,e] </p>
                    <p>The Equivalence Relation is: [['a', 'a'], ['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'b'], ['b', 'c'], <br/>
                        ['c', 'a'], ['c', 'b'], ['c', 'c'], ['d', 'd'], ['d', 'e'], ['e', 'd'], ['e', 'e']]
                    </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );


};

export default Equivalence