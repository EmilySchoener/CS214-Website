// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const OrderOfMagnitude = () => {

    const [f, setF] = useState("");
    const [g, setG] = useState("");
    const [x, setX] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
           // alert (`Partition 1 ${part1}, Partition 2: ${part2} Set: ${set}`,);
            const response = await axios.post("http://127.0.0.1:5000/submitOrderOfMag", {
                f,
                g,
                x,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }

    }

     const FChange= (e) => {
        setF(e.target.value);
    }

     const GChange= (e) => {
        setG(e.target.value);
    }

      const XChange= (e) => {
        setX(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitOrderOfMag")
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
                5.5 - Order of Magnitude webpage.
            </h1>
            <Splitter>
                <SplitterPanel>
                    <p> Note: If you want to type in exponents, please use ** as a stand in for ^, for instance x^2
                        would be x**2</p>
                    <p> If the function is 3x, please enter it as 3*x</p>
                    <p> If the function uses square root, such as sqrt(x +100), please enter it as x**1/2 + 100**1/2</p>
                    <p> If you are pressing submit and it still says Loading, ensure the value of X0 is not equal to or less than 0, or
                    confirm that you have entered a function for both f and g</p>
                    <form onSubmit={handleSubmit}>
                        <label> Type in the function of f:
                            <input

                                onChange={FChange}
                                placeholder="Enter the function of f"
                            />
                        </label>
                        <br/>
                        <label> Type in the function of g:
                            <input
                                onChange={GChange}
                                placeholder="Enter the function of g"
                            />
                        </label>
                        <br/>
                        <label> Type in the value of X0 for the functions to use:
                            <input
                                onChange={XChange}
                                placeholder="Enter the value of X0"
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
                            C1 = {responseData[0]}<br/>
                            C2 = {responseData[1]}<br/>
                            nO = {responseData[2]}
                        </ul>
                    ) : (
                        <p> ... Loading ...</p>
                    )}
                </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>Type in the function of f: 3*x**3-7*x</p>
                    <p>Type in the function of g: x**3/2</p>
                    <p>Type in the value of X0 for the functions to use: 1</p>
                    <p> C1 = 2
                    </p>
                    <p> C2 = 3
                    </p>
                    <p> C2 = 4
                    </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );


};

export default OrderOfMagnitude