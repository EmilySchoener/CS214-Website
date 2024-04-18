import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const ReachabilityMatrix = () => {
    const [algo, setAlgo] = useState("1");

    const [oneOne, setOneOne] = useState("");
    const [oneTwo, setOneTwo] = useState("");
    const [oneThree, setOneThree] = useState("");
    const [oneFour, setOneFour] = useState("");
    const [oneFive, setOneFive] = useState("");

    const [twoOne, setTwoOne] = useState("");
    const [twoTwo, setTwoTwo] = useState("");
    const [twoThree, setTwoThree] = useState("");
    const [twoFour, setTwoFour] = useState("");
    const [twoFive, setTwoFive] = useState("");

    const [threeOne, setThreeOne] = useState("");
    const [threeTwo, setThreeTwo] = useState("");
    const [threeThree, setThreeThree] = useState("");
    const [threeFour, setThreeFour] = useState("");
    const [threeFive, setThreeFive] = useState("");

    const [fourOne, setFourOne] = useState("");
    const [fourTwo, setFourTwo] = useState("");
    const [fourThree, setFourThree] = useState("");
    const [fourFour, setFourFour] = useState("");
    const [fourFive, setFourFive] = useState("");

    const [fiveOne, setFiveOne] = useState("");
    const [fiveTwo, setFiveTwo] = useState("");
    const [fiveThree, setFiveThree] = useState("");
    const [fiveFour, setFiveFour] = useState("");
    const [fiveFive, setFiveFive] = useState("");

    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/7_1_3", {
                algo,
                oneOne,
                oneTwo,
                oneThree,
                oneFour,
                oneFive,
                twoOne,
                twoTwo,
                twoThree,
                twoFour,
                twoFive,
                threeOne,
                threeTwo,
                threeThree,
                threeFour,
                threeFive,
                fourOne,
                fourTwo,
                fourThree,
                fourFour,
                fourFive,
                fiveOne,
                fiveTwo,
                fiveThree,
                fiveFour,
                fiveFive,
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
    const oneOneChange= (e) => {
        setOneOne(e.target.value);
    }
    const oneTwoChange= (e) => {
        setOneTwo(e.target.value);
    }
    const oneThreeChange= (e) => {
        setOneThree(e.target.value);
    }
    const oneFourChange= (e) => {
        setOneFour(e.target.value);
    }
    const oneFiveChange= (e) => {
        setOneFive(e.target.value);
    }
    const twoOneChange= (e) => {
        setTwoOne(e.target.value);
    }
    const twoTwoChange= (e) => {
        setTwoTwo(e.target.value);
    }
    const twoThreeChange= (e) => {
        setTwoThree(e.target.value);
    }
    const twoFourChange= (e) => {
        setTwoFour(e.target.value);
    }
    const twoFiveChange= (e) => {
        setTwoFive(e.target.value);
    }
    const threeOneChange= (e) => {
        setThreeOne(e.target.value);
    }
    const threeTwoChange= (e) => {
        setThreeTwo(e.target.value);
    }
    const threeThreeChange= (e) => {
        setThreeThree(e.target.value);
    }
    const threeFourChange= (e) => {
        setThreeFour(e.target.value);
    }
    const threeFiveChange= (e) => {
        setThreeFive(e.target.value);
    }
    const fourOneChange= (e) => {
        setFourOne(e.target.value);
    }
    const fourTwoChange= (e) => {
        setFourTwo(e.target.value);
    }
    const fourThreeChange= (e) => {
        setFourThree(e.target.value);
    }
    const fourFourChange= (e) => {
        setFourFour(e.target.value);
    }
    const fourFiveChange= (e) => {
        setFourFive(e.target.value);
    }
    const fiveOneChange= (e) => {
        setFiveOne(e.target.value);
    }
    const fiveTwoChange= (e) => {
        setFiveTwo(e.target.value);
    }
    const fiveThreeChange= (e) => {
        setFiveThree(e.target.value);
    }
    const fiveFourChange= (e) => {
        setFiveFour(e.target.value);
    }
    const fiveFiveChange= (e) => {
        setFiveFive(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/7_1_3")
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
                Chapter 7.1 - Reachability Matrix From Matrix
            </h1>
            <form onSubmit={handleSubmit}>
                Which algorithm would you like to use to find the reachability matrix?
                <select id="dropdown" value={algo} onChange={algoChange}>
                    <option value="1">Custom Algo</option>
                    <option value="2">Warshall's Algo</option>
                </select>
                <br/>*Note: The Custom Algo is R = A V A<sup>(2)</sup> V ... V A<sup>(n)</sup>
                <br/>
                <label>
                    <input
                        onChange={oneOneChange}
                        type="text"
                        value={oneOne}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={oneTwoChange}
                        type="text"
                        value={oneTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={oneThreeChange}
                        type="text"
                        value={oneThree}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={oneFourChange}
                        type="text"
                        value={oneFour}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={oneFiveChange}
                        type="text"
                        value={oneFive}
                        style={{ width: "40px" }}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={twoOneChange}
                        type="text"
                        value={twoOne}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={twoTwoChange}
                        type="text"
                        value={twoTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={twoThreeChange}
                        type="text"
                        value={twoThree}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={twoFourChange}
                        type="text"
                        value={twoFour}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={twoFiveChange}
                        type="text"
                        value={twoFive}
                        style={{ width: "40px" }}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={threeOneChange}
                        type="text"
                        value={threeOne}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={threeTwoChange}
                        type="text"
                        value={threeTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={threeThreeChange}
                        type="text"
                        value={threeThree}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={threeFourChange}
                        type="text"
                        value={threeFour}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={threeFiveChange}
                        type="text"
                        value={threeFive}
                        style={{ width: "40px" }}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={fourOneChange}
                        type="text"
                        value={fourOne}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fourTwoChange}
                        type="text"
                        value={fourTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fourThreeChange}
                        type="text"
                        value={fourThree}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fourFourChange}
                        type="text"
                        value={fourFour}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fourFiveChange}
                        type="text"
                        value={fourFive}
                        style={{ width: "40px" }}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={fiveOneChange}
                        type="text"
                        value={fiveOne}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fiveTwoChange}
                        type="text"
                        value={fiveTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fiveThreeChange}
                        type="text"
                        value={fiveThree}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fiveFourChange}
                        type="text"
                        value={fiveFour}
                        style={{ width: "40px" }}
                    />
                </label>
                <label>
                    <input
                        onChange={fiveFiveChange}
                        type="text"
                        value={fiveFive}
                        style={{ width: "40px" }}
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
            {responseData !== null ? (
                <p>{responseData}</p>
            ) : (
                <p>Loading...</p>
            )}

        </div>
    );
};

export default ReachabilityMatrix