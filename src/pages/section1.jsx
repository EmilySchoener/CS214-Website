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
            setError("Please enter a Well Formed Formula.");
            return;
        }
        try {
            const response = await axios.post("http://127.0.0.1:5000/submitwff", { S, A, B, C, truthTable });
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

    const handleRadioChange = (e) => {
        const { name, value } = e.target;
        if (name === "A") {
            setA(value === "true");
        } else if (name === "B") {
            setB(value === "true");
        } else if (name === "C") {
            setC(value === "true");
        }
    };

    const handleToggleChange = () => {
        setTruthTable(!truthTable); // Toggle the truth table value
        setResponseData(null); // Reset responseData to null
        setError(null); // Reset error to null
    };

    return (
        <div>
            <h1>Section 1.1 webpage.</h1>
            <Splitter>
                <SplitterPanel>
                    <label htmlFor="toggle">Truth Table:</label>
                    <input
                        type="checkbox"
                        id="toggle"
                        checked={truthTable}
                        onChange={handleToggleChange}
                    />
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
                    <p>Truth Table Checked </p>
                    <p>Input: ( A - B ) = A ' * B </p>
                    <pre>B|	A|	( A - B ) = A ' * B </pre>
                    <pre>True|	True|	T</pre>
                    <pre>True|	False|	T</pre>
                    <pre>False|	True|	T </pre>
                    <pre>False|	False|	T</pre>
                    <pre>Tautology</pre>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default Section1_1;