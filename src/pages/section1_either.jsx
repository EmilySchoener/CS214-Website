import React, { useState } from "react";
import { Splitter, SplitterPanel } from 'primereact/splitter';
const Section1Either = () => {
    const [choice, setChoice] = useState("either");
    const [text, setText] = useState("");

    const handleChoiceChange = (e) => {
        setChoice(e.target.value);
    }

    const handleInputChange = (e) => {
        setText(e.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Choice: ${choice}\nText: ${text}`);
    }

    return (
        <div>
            <h1>
                Section 1 - Either Page
            </h1>
            <Splitter>
                <SplitterPanel>
            <p>Choose Either or Neither:</p>
            <form onSubmit={handleSubmit}>
                <div>
                    <input
                        type="radio"
                        id="either"
                        value="A or B"
                        checked={choice === "A or B"}
                        onChange={handleChoiceChange}
                    />
                    <label htmlFor="either">Either</label>
                </div>
                <div>
                    <input
                        type="radio"
                        id="neither"
                        value="Not A and  Not B"
                        checked={choice === "Not A and  Not B"}
                        onChange={handleChoiceChange}
                    />
                    <label htmlFor="neither">Neither</label>
                </div>
                <button type="submit">Submit</button>
            </form>
            <p>
                Choice: {choice}<br />
            </p>
                </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                </SplitterPanel>
            </Splitter>
        </div>
    );
};

export default Section1Either;