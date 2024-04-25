import React, { useState } from "react";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';

const Section1_1 = () => {
    const [S, setS] = useState("");
    const [A, setA] = useState(false);
    const [B, setB] = useState(false);
    const [C, setC] = useState(false);
    const [responseData, setResponseData] = useState(null);
    const [error, setError] = useState(null);
    const [truthTable, setTruthTable] = useState(true); // Initial value of truth table toggle

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!S.trim()) {
            setError("Please enter a Well Formed Formula Proof.");
            return;
        }
        try {
            const response = await axios.post("http://127.0.0.1:5000/submitproof", { S });
            setResponseData(response.data.result); // Ensure that response data is properly set
            setError(null);
        } catch (error) {
            console.error("Error:", error);
            setError("An error occurred while processing the request.");
            setResponseData(null);
        }
    };

    const handleInputChange = (e) => {
        setS(e.target.value);
        if (error) {
            setError(null); // Clear error message when user starts typing
        }
    };
    
    

    return (
        <div>
            <h1>Section 1.1 webpage.</h1>
            <Splitter>
                <SplitterPanel>
                    <br/>
                    <form onSubmit={handleSubmit}>
                        <label htmlFor="inputField">Input:</label>
                        <input
                            type="text"
                            id="inputField"
                            value={S}
                            onChange={handleInputChange}
                            placeholder="Enter a Well Formed Formula"
                        />
                        <br/>
                        {!truthTable && (
                            <>
                                <label htmlFor="radioA">A:</label>
                                <input
                                    type="radio"
                                    id="radioA"
                                    name="A"
                                    value="true"
                                    checked={A}
                                    onChange={handleRadioChange}
                                />
                                True
                                <input
                                    type="radio"
                                    id="radioA"
                                    name="A"
                                    value="false"
                                    checked={!A}
                                    onChange={handleRadioChange}
                                />
                                False
                                <br/>
                                <label htmlFor="radioB">B:</label>
                                <input
                                    type="radio"
                                    id="radioB"
                                    name="B"
                                    value="true"
                                    checked={B}
                                    onChange={handleRadioChange}
                                />
                                True
                                <input
                                    type="radio"
                                    id="radioB"
                                    name="B"
                                    value="false"
                                    checked={!B}
                                    onChange={handleRadioChange}
                                />
                                False
                                <br/>
                                <label htmlFor="radioC">C:</label>
                                <input
                                    type="radio"
                                    id="radioC"
                                    name="C"
                                    value="true"
                                    checked={C}
                                    onChange={handleRadioChange}
                                />
                                True
                                <input
                                    type="radio"
                                    id="radioC"
                                    name="C"
                                    value="false"
                                    checked={!C}
                                    onChange={handleRadioChange}
                                />
                                False
                                <br/>
                            </>
                        )}
                        <button type="submit">Submit</button>
                    </form>
                    {error && (
                        <div>
                            <h2>Error:</h2>
                            <p>{error}</p>
                        </div>
                    )}
                    {responseData !== null && (
                        <div>
                            <h2>Output:</h2>
                            <pre>{responseData}</pre>
                        </div>
                    )}
                </SplitterPanel>
                <SplitterPanel>
                    <h2>Key:</h2>
                    <p>Ensure every character is seperated by a space </p>
                    <p>Statement Letters: A B C </p>
                    <p>Conjunction: & </p>
                    <p>Disjunction: * </p>
                    <p>Implication: - </p>
                    <p>Equivalence: = </p>
                    <p>Negation: '</p>
                </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>Input: ( A & B ' ) & C = ( A & C ) & B ' </p>
                    <pre>A & ( B ' & C ) by 2b</pre>
                    <pre>A & ( C & B ' ) by 1b</pre>
                    <pre>( A & C ) & B ' by 2b</pre>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default Section1_1;