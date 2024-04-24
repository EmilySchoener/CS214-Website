// Filename - pages/5_5pages/MasterTheorem.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const MasterTheorem = () => {

    const [a, setA] = useState("");
    const [b, setB] = useState("");
    const [c, setC] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
           // alert (`Partition 1 ${part1}, Partition 2: ${part2} Set: ${set}`,);
            const response = await axios.post("http://127.0.0.1:5000/submitMasterTheorem", {
                a,
                b,
                c,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }

    }

     const AChange= (e) => {
        setA(e.target.value);
    }

     const BChange= (e) => {
        setB(e.target.value);
    }

      const CChange= (e) => {
        setC(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitMasterTheorem")
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
                5.5 - Master Theorem webpage.
            </h1>
            <Splitter>
                <SplitterPanel>
            <p> Note: The form of a recurrence relation is S(n) = aS(n/b) + n^c for n is equal to or greater than 2</p>
                    <p> If the recurrence relation you are typing in is the square root of n, please enter .5 for c</p>
            <form onSubmit={handleSubmit}>
                <label> Type in the value of a:
                    <input

                        onChange={AChange}
                        placeholder="Enter the value of a"
                    />
                </label>
                <br/>
                <label> Type in the value of b:
                <input
                    onChange={BChange}
                    placeholder="Enter the value of b"
                />
                    </label>
                <br/>
                <label> Type in the value of c where c is the exponent of n in the function:
                <input
                    onChange={CChange}
                    placeholder="Enter the value of c"
                />
                    </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>
            <h2>Solution</h2>
            Order of Magnitude is: {responseData}
            </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>Type in the value of a: 4 </p>
                    <p>Type in the value of b: 4 </p>
                    <p>Type in the value of c where c is the exponent of n in the function: 2 </p>
                    <p> Order of Magnitude is: S(n) = O(n^2)
                    </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );


};

export default MasterTheorem