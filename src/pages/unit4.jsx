// Filename - pages/unit4.jsx
import React from "react";
import { Link } from 'react-router-dom'
import { experimentalStyled as styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Card from "react-bootstrap/Card";
import ListGroup from 'react-bootstrap/ListGroup';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#546581',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
    maxWidth: 400,
    minHeight: 220,
  color: theme.palette.text.secondary,
}));

const sections = [
    {
        id: 1,
        title: "True or False given Sets and Condition",
        content: "Solves Example: 3 and Homework: 11-16",
        link: "/unit4/TrueOrFalse"
    },
    {
        id: 2,
        title: "Power Set",
        content: "Solves Example: 6, Practice: 8, and Homework: 27-32",
        link: "/unit4/PowerSet"
    },
    {
        id: 3,
        title: "Binary or Unary",
        content: "Solves Homework: 40b",
        link: "/unit4/BinaryOrUnary"
    },
    {
        id: 4,
        title: "Solve Expressions",
        content: "Solves Example: 16, Practice: 16, and Homework: 47-51",
        link: "/unit4/SolveExpression"
    }
    ]

const Unit4 = () => {

    return (
        <div>
            <h1>
                Section 4.1
            </h1>
            <h2>Problems</h2>
            <Box sx={{flexGrow: 1}}>
                <Grid container spacing={1} columns={{xs: 2, sm: 10, md: 15}}>
                    {sections.map((unit, index) => (
                        <Grid item xs={2} sm={4} md={4} key={index}>
                            <Item>
                                <Card>
                                    <h2>{unit.title}</h2>
                                    <p>{unit.content}</p>
                                    <br/>
                                </Card>
                                <a href={unit.link}>
                                    <button> Go To {unit.title} </button>
                                </a>
                            </Item>
                        </Grid>
                    ))}
                </Grid>
            </Box>
        </div>
    );
};

export default Unit4;