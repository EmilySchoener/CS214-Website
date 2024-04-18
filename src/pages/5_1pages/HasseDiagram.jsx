// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';
import Hasse from "../../../backend/Hasse.png";

const HasseDiagram = () => {

    const [S, setS] = useState("");
    const [responseData, setResponseData] = useState(null);
    const [imageUrl, setImageUrl] = useState('');
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            alert (`S List: ${S}`);
            const response = await axios.post("http://127.0.0.1:5000/submitHasse", {
                S,
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


    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitHasse")
      .then(response => {
        // Update the state with the response data
        setImageUrl(response.data);
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
                5.1 - Hasse Diagram webpage.
            </h1>
                    <p> Input: </p>
                    <form onSubmit={handleSubmit}>
                        <label> Type in the Pairs of the Partial Ordering:
                            <input

                                onChange={sChange}
                                placeholder="Enter the pairs in the partial ordering"
                            />
                        </label>
                        <br/>
                        <button
                            type="submit">
                            Submit
                        </button>
                    </form>
                    <h2>Solution</h2>

                    {imageUrl && <img src={imageUrl} alt="Hasse Diagram" />}
        </div>
    );
};

export default HasseDiagram