import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const BinaryOrUnary = () => {
    const [set, setSet] = useState([]);
    const [oneOne, setOneOne] = useState("");
    const [oneTwo, setOneTwo] = useState("");
    const [oneThree, setOneThree] = useState("");
    const [twoOne, setTwoOne] = useState("");
    const [twoTwo, setTwoTwo] = useState("");
    const [twoThree, setTwoThree] = useState("");
    const [threeOne, setThreeOne] = useState("");
    const [threeTwo, setThreeTwo] = useState("");
    const [threeThree, setThreeThree] = useState("");
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/4_1_3", {
                set,
                oneOne,
                oneTwo,
                oneThree,
                twoOne,
                twoTwo,
                twoThree,
                threeOne,
                threeTwo,
                threeThree
            });
            console.log("Response from server:", response.data);
        } catch (error) {
            console.error("Error:", error);
        }
        window.location.reload();
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
    const twoOneChange= (e) => {
        setTwoOne(e.target.value);
    }
    const twoTwoChange= (e) => {
        setTwoTwo(e.target.value);
    }
    const twoThreeChange= (e) => {
        setTwoThree(e.target.value);
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

    useEffect(() => {
        // Make an HTTP GET request to your Flask backend when the component mounts
        axios.get("http://127.0.0.1:5000/4_1_3")
          .then(response => {
            // Update the state with the response data
            setResponseData(response.data);
          })
          .catch(error => {
            // Handle any errors
            console.error('Error fetching data:', error);
          });
    }, []);

    return (
        <div>
            <h1>
                4.1 - Binary Or Unary Webpage.
            </h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Set =
                    <input
                        onChange={setChange}
                        type="text"
                        value={set}
                        placeholder="Enter elements of set here"
                    />
                </label>
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

export default BinaryOrUnary;