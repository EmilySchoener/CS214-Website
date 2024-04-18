// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const MMLGElements= () => {

    const [S, setS] = useState("");
    const [set, setInitial] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            alert (`S List: ${S}`);
            const response = await axios.post("http://127.0.0.1:5000/submitMMLG", {
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
    axios.get("http://localhost:5000/submitMMLG")
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
                5.1 - Maximal, Minimal, Least, Greatest webpage.
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
                        <label> Type in the Pairs of the Partial Ordering:
                            <input

                                onChange={sChange}
                                placeholder="Enter the pairs of the partial ordering"
                            />
                        </label>
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
                    <p>Type in the Initial Set S: [1,2,4,5,6] </p>
                    <p>Type in the Pairs of the relation: [[1,2],[3,4],[5,7]] </p>
                    <p>The list of S is not reflexive <br/>
                        The list of S is irreflexive<br/>
                        The list of S is not symmetric<br/>
                        The list of S is not antisymmetric<br/>
                        The list of S is not transitive<br/>
                        The list of S is not asymmetric<br/>
                        The list of S is not an equivalence relation</p>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default MMLGElements