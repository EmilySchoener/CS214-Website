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
        content: "TBD",
        link: "/unit4/TrueOrFalse"
    },
    {
        id: 2,
        title: "Power Set",
        content: "TBD",
        link: "/unit4/PowerSet"
    },
    {
        id: 3,
        title: "Binary or Unary",
        content: "TBD",
        link: "/unit4/BinaryOrUnary"
    },
    {
        id: 4,
        title: "Solve Expressions",
        content: "TBD",
        link: "/unit4/SolveExpression"
    }
    ]

const Unit4 = () => {

    return (
        <div>
            <h1>
                Chapter 4.1
            </h1>
            <h2>Problems</h2>
            <Box sx={{flexGrow: 1}}>
                <Grid container spacing={1} columns={{xs: 2, sm: 10, md: 15}}>
                    {sections.map((unit, index) => (
                        <Grid item xs={2} sm={4} md={4} key={index}>
                            <Item>
                                <Card>
                                    <h2>{unit.title}</h2>
                                    <span style={{fontSize: 14, fontWeight: 'bold'}}><p>{unit.content}</p></span>
                                    <br/>
                                    <p>Add descriptor or example image.</p>
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