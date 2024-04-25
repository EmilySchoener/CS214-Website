import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

const BooleanMatrices = () => {
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

    const [mat_2oneOne, mat_2setOneOne] = useState("");
    const [mat_2oneTwo, mat_2setOneTwo] = useState("");
    const [mat_2oneThree, mat_2setOneThree] = useState("");
    const [mat_2oneFour, mat_2setOneFour] = useState("");

    const [mat_2twoOne, mat_2setTwoOne] = useState("");
    const [mat_2twoTwo, mat_2setTwoTwo] = useState("");
    const [mat_2twoThree, mat_2setTwoThree] = useState("");
    const [mat_2twoFour, mat_2setTwoFour] = useState("");

    const [mat_2threeOne, mat_2setThreeOne] = useState("");
    const [mat_2threeTwo, mat_2setThreeTwo] = useState("");
    const [mat_2threeThree, mat_2setThreeThree] = useState("");
    const [mat_2threeFour, mat_2setThreeFour] = useState("");

    const [mat_2fourOne, mat_2setFourOne] = useState("");
    const [mat_2fourTwo, mat_2setFourTwo] = useState("");
    const [mat_2fourThree, mat_2setFourThree] = useState("");
    const [mat_2fourFour, mat_2setFourFour] = useState("");


    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/submitBoolMatrix", {
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
                mat_2oneOne,
                mat_2oneTwo,
                mat_2oneThree,
                mat_2oneFour,
                mat_2twoOne,
                mat_2twoTwo,
                mat_2twoThree,
                mat_2twoFour,
                mat_2threeOne,
                mat_2threeTwo,
                mat_2threeThree,
                mat_2threeFour,
                mat_2fourOne,
                mat_2fourTwo,
                mat_2fourThree,
                mat_2fourFour,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }
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


    const  mat_2oneOneChange= (e) => {
         mat_2setOneOne(e.target.value);
    }
    const  mat_2oneTwoChange= (e) => {
         mat_2setOneTwo(e.target.value);
    }
    const  mat_2oneThreeChange= (e) => {
         mat_2setOneThree(e.target.value);
    }
    const  mat_2oneFourChange= (e) => {
         mat_2setOneFour(e.target.value);
    }
    const  mat_2twoOneChange= (e) => {
         mat_2setTwoOne(e.target.value);
    }
    const  mat_2twoTwoChange= (e) => {
         mat_2setTwoTwo(e.target.value);
    }
    const  mat_2twoThreeChange= (e) => {
         mat_2setTwoThree(e.target.value);
    }
    const  mat_2twoFourChange= (e) => {
         mat_2setTwoFour(e.target.value);
    }
    const  mat_2threeOneChange= (e) => {
         mat_2setThreeOne(e.target.value);
    }
    const  mat_2threeTwoChange= (e) => {
         mat_2setThreeTwo(e.target.value);
    }
    const  mat_2threeThreeChange= (e) => {
         mat_2setThreeThree(e.target.value);
    }
    const  mat_2threeFourChange= (e) => {
         mat_2setThreeFour(e.target.value);
    }
    const  mat_2fourOneChange= (e) => {
         mat_2setFourOne(e.target.value);
    }
    const  mat_2fourTwoChange= (e) => {
         mat_2setFourTwo(e.target.value);
    }
    const  mat_2fourThreeChange= (e) => {
         mat_2setFourThree(e.target.value);
    }
    const  mat_2fourFourChange= (e) => {
         mat_2setFourFour(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitBoolMatrix")
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
                Chapter 5.7 Boolean Matrices
            </h1>
            <form onSubmit={handleSubmit}>
                <p>Note: For reading the output, a matrix row is from the start and end of a [  ] representation
                    For instance, a 2x2 matrix would be [0 0][0 0]</p>
                <br/>
                Please enter A below, if you would like to use a 2x2 or 3x3 matrix please leave "-" in the empty spaces.
                <br/>
                <label>
                    <input
                        onChange={oneOneChange}
                        type="text"
                        value={oneOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={oneTwoChange}
                        type="text"
                        value={oneTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={oneThreeChange}
                        type="text"
                        value={oneThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={oneFourChange}
                        type="text"
                        value={oneFour}
                        style={{width: "40px"}}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={twoOneChange}
                        type="text"
                        value={twoOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={twoTwoChange}
                        type="text"
                        value={twoTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={twoThreeChange}
                        type="text"
                        value={twoThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={twoFourChange}
                        type="text"
                        value={twoFour}
                        style={{width: "40px"}}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={threeOneChange}
                        type="text"
                        value={threeOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={threeTwoChange}
                        type="text"
                        value={threeTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={threeThreeChange}
                        type="text"
                        value={threeThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={threeFourChange}
                        type="text"
                        value={threeFour}
                        style={{width: "40px"}}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={fourOneChange}
                        type="text"
                        value={fourOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={fourTwoChange}
                        type="text"
                        value={fourTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={fourThreeChange}
                        type="text"
                        value={fourThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={fourFourChange}
                        type="text"
                        value={fourFour}
                        style={{width: "40px"}}
                    />
                </label>
                <br/>
                <br/>
                Please enter B below, if you would like to use a 2x2 or 3x3 matrix please leave "-" in the empty spaces.
                <br/>
                <label>
                    <input
                        onChange={mat_2oneOneChange}
                        type="text"
                        value={mat_2oneOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2oneTwoChange}
                        type="text"
                        value={mat_2oneTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2oneThreeChange}
                        type="text"
                        value={mat_2oneThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2oneFourChange}
                        type="text"
                        value={mat_2oneFour}
                        style={{width: "40px"}}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={mat_2twoOneChange}
                        type="text"
                        value={mat_2twoOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2twoTwoChange}
                        type="text"
                        value={mat_2twoTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2twoThreeChange}
                        type="text"
                        value={mat_2twoThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2twoFourChange}
                        type="text"
                        value={mat_2twoFour}
                        style={{width: "40px"}}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={mat_2threeOneChange}
                        type="text"
                        value={mat_2threeOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2threeTwoChange}
                        type="text"
                        value={mat_2threeTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2threeThreeChange}
                        type="text"
                        value={mat_2threeThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2threeFourChange}
                        type="text"
                        value={mat_2threeFour}
                        style={{width: "40px"}}
                    />
                </label>
                <br/>
                <label>
                    <input
                        onChange={mat_2fourOneChange}
                        type="text"
                        value={mat_2fourOne}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2fourTwoChange}
                        type="text"
                        value={mat_2fourTwo}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2fourThreeChange}
                        type="text"
                        value={mat_2fourThree}
                        style={{width: "40px"}}
                    />
                </label>
                <label>
                    <input
                        onChange={mat_2fourFourChange}
                        type="text"
                        value={mat_2fourFour}
                        style={{width: "40px"}}
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
                <div>
                    {responseData.map((item, index) => (
                        <div key={index}>{item}</div>
                    ))}
                </div>
            ) : (
                <p> ... Loading ...</p>
            )}

        </div>
    );
};

export default BooleanMatrices