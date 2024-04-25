import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';

const BinaryOrUnary = () => {
    const [set, setSet] = useState("1,2,3");
    const [oneOne, setOneOne] = useState("1");
    const [oneTwo, setOneTwo] = useState("2");
    const [oneThree, setOneThree] = useState("3");
    const [twoOne, setTwoOne] = useState("2");
    const [twoTwo, setTwoTwo] = useState("3");
    const [twoThree, setTwoThree] = useState("4");
    const [threeOne, setThreeOne] = useState("3");
    const [threeTwo, setThreeTwo] = useState("4");
    const [threeThree, setThreeThree] = useState("5");
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
            fetchData()
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

    const fetchData = () => {
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
    }

    useEffect(() => {
        fetchData()
    }, []);

    return (
        <div>
            <h1>
                4.1 - Binary Or Unary Webpage.
            </h1>
            <Splitter>
                <SplitterPanel>
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
                    Enter elements of your matrix here: <br/>
                    <input
                        onChange={oneOneChange}
                        type="text"
                        value={oneOne}
                        style={{ width: "40px" }}
                    />
                </label>
                {" "}
                <label>
                    <input
                        onChange={oneTwoChange}
                        type="text"
                        value={oneTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                {" "}
                <label>
                    <input
                        onChange={oneThreeChange}
                        type="text"
                        value={oneThree}
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
                {" "}
                <label>
                    <input
                        onChange={twoTwoChange}
                        type="text"
                        value={twoTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                {" "}
                <label>
                    <input
                        onChange={twoThreeChange}
                        type="text"
                        value={twoThree}
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
                {" "}
                <label>
                    <input
                        onChange={threeTwoChange}
                        type="text"
                        value={threeTwo}
                        style={{ width: "40px" }}
                    />
                </label>
                {" "}
                <label>
                    <input
                        onChange={threeThreeChange}
                        type="text"
                        value={threeThree}
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
            {responseData !== null ? (
                <p>{responseData}</p>
            ) : (
                <p>Loading...</p>
            )}
                </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>
                        Set = 1,2,3<br/>
                        Matrix = <br/>
                        1 2 3 <br/>
                        2 3 4 <br/>
                        3 4 5 <br/>
                    </p>
                    <p>
                        Solution: <br/>
                        False, did not find 4 in set
                    </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default BinaryOrUnary;