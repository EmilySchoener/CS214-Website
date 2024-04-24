// Filename - pages/5_1pages/MMLG.jsx
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
            const setArray = set.match(/\w+/g);
            const SArray = S.split('],[').map(item => item.replace(/[\[\]']+/g, '').split(','));
            console.log("setArray:", setArray);
            alert(`S List: ${S}`);
            const response = await axios.post("http://127.0.0.1:5000/submitMMLG", {
                S: SArray,
                set: setArray,
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
          console.log("Response data from backend:", response.data);
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
                        <label> Type in the Initial Set:
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
                    <p>Type in the Initial Set: ['a','b','c'] </p>
                    <p>Type in the Pairs of the Partial Ordering: [['a','a'],['b','b'],['c','c'],['a','b'],['b','c'],['a','c']] </p>
                    <p>The element a is a minimal element in the partial ordering <br/>
                        The element b is a maximal element in the partial ordering<br/>
                        The element c is a maximal element in the partial ordering<br/>
                        The least element is a<br/>
                        The greatest element is c<br/>
                       </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default MMLGElements