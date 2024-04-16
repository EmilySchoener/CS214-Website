import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const MatrixSquared = () => {
    const [set, setSet] = useState([]);
    const [oneOne, setOneOne] = useState("");
    const [oneTwo, setOneTwo] = useState("");
    const [oneThree, setOneThree] = useState("");
    const [oneFour, setOneFour] = useState("");

    const [twoOne, setTwoOne] = useState("");
    const [twoTwo, setTwoTwo] = useState("");
    const [twoThree, setTwoThree] = useState("");
    const [twoFour, setTwoFour] = useState("");

    const [threeOne, setThreeOne] = useState("");
    const [threeTwo, setThreeTwo] = useState("");
    const [threeThree, setThreeThree] = useState("");
    const [threeFour, setThreeFour] = useState("");

    const [fourOne, setFourOne] = useState("");
    const [fourTwo, setFourTwo] = useState("");
    const [fourThree, setFourThree] = useState("");
    const [fourFour, setFourFour] = useState("");
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/7_1_2", {
                set,
                oneOne,
                oneTwo,
                oneThree,
                oneFour,
                twoOne,
                twoTwo,
                twoThree,
                twoFour,
                threeOne,
                threeTwo,
                threeThree,
                threeFour,
                fourOne,
                fourTwo,
                fourThree,
                fourFour,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const setChange= (e) => {
        setSet(e.target.value);
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

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/7_1_2")
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
                Chapter 7.1 - Matrix Squared
            </h1>
            <form onSubmit={handleSubmit}>
                This will find products A^2 and A^(2) given A.
                <br/>
                Please enter A below, if you would like to use a 3x3 matrix please leave "-" in the empty spaces.
                <br/>
                <label>
                    <input
                        onChange={oneOneChange}
                        type="text"
                        value={oneOne}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={oneTwoChange}
                        type="text"
                        value={oneTwo}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={oneThreeChange}
                        type="text"
                        value={oneThree}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={oneFourChange}
                        type="text"
                        value={oneFour}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={twoOneChange}
                        type="text"
                        value={twoOne}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={twoTwoChange}
                        type="text"
                        value={twoTwo}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={twoThreeChange}
                        type="text"
                        value={twoThree}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={twoFourChange}
                        type="text"
                        value={twoFour}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={threeOneChange}
                        type="text"
                        value={threeOne}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={threeTwoChange}
                        type="text"
                        value={threeTwo}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={threeThreeChange}
                        type="text"
                        value={threeThree}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={threeFourChange}
                        type="text"
                        value={threeFour}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={fourOneChange}
                        type="text"
                        value={fourOne}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={fourTwoChange}
                        type="text"
                        value={fourTwo}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={fourThreeChange}
                        type="text"
                        value={fourThree}
                        placeholder="Enter element of matrix here"
                    />
                </label>
                <label>
                    <input
                        onChange={fourFourChange}
                        type="text"
                        value={fourFour}
                        placeholder="Enter element of matrix here"
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

export default MatrixSquared