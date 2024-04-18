import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const WarshallReachability = () => {
    const [algo, setAlgo] = useState("1");
    const [set, setSet] = useState([])
    const [relation, setRelation] = useState([]);
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/7_1_4", {
                algo,
                set,
                relation,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const algoChange= (e) => {
        setAlgo(e.target.value);
    }
    const setChange= (e) => {
        setSet(e.target.value);
    }
    const relationChange= (e) => {
        setRelation(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/7_1_4")
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

    return (
        <div>
            <h1>
                Chapter 7.1 - Reachability Matrix Form Relation and Set
            </h1>
            <form onSubmit={handleSubmit}>
                Which algorithm would you like to use to find the reachability matrix?
                <select id="dropdown" value={algo} onChange={algoChange}>
                    <option value="1">Custom Algo</option>
                    <option value="2">Warshall's Algo</option>
                </select>
                <br/><br/>
                <label>Give the adjacency relation <br/> p =
                    <input
                        onChange={relationChange}
                        type="text"
                        value={relation}
                        placeholder="Enter Here"
                    />
                </label>
                <br/>
                <label><br/>On the set N. Please enter each element separated by a comma. <br/> N=
                    <input
                        onChange={setChange}
                        type="text"
                        value={set}
                        placeholder="Enter each element separated by a comma"
                    />
                </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>


        </div>
    );
};

export default WarshallReachability