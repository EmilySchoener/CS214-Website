// Filename - pages/ErrorReport.jsx
import React, {useState} from "react";
import axios from "axios";
import emailjs from '@emailjs/browser';


const Report = () => {
    const [formData, setFormData] = useState({
        from_name: '',
        email: '',
        message: ''
    });


    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
       emailjs.send("service_4ub3vtt","template_m34ykds",{
                    from_name: formData.from_name,
                    email: formData.email,
                    message: formData.message}, {
        publicKey: 'TtHOty0oV0DN0RUEr',
      })
      .then(
        () => {
          alert('Email Sent!');
        },
        (error) => {
          alert('Email failed to send.');
        },
      );
        try {
            const response = await axios.post('http://localhost:5000/submit', formData);
            console.log('Response from server:', response.data);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <h1>User Input</h1>
            <h2>Want to report an error or share input?</h2>
            <br/>
            <h2>Fill out this form:</h2>

            <form onSubmit={handleSubmit}>
                <label>Name:
                    <input type="text" name="name" value={formData.name} onChange={handleChange}/> </label> <br/>
                <label>Email:
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required/></label> <br/>
                <p>Message:</p>
                    <textarea name="message" cols={35} rows={10} value={formData.message}
                              onChange={handleChange}/><br/>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default Report;