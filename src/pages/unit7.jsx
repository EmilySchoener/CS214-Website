// Filename - pages/unit7.jsx
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
        title: "Different Graphs",
        content: "TBD",
        link: "/unit7/DifferentGraphs"
    },
    {
        id: 2,
        title: "Matrix Squared",
        content: "TBD",
        link: "/unit7/MatrixSquared"
    },
    {
        id: 3,
        title: "Reachability Matrix From Matrix",
        content: "TBD",
        link: "/unit7/ReachabilityMatrix"
    },
    {
        id: 4,
        title: "Reachability Matrix From Relation and Set",
        content: "TBD",
        link: "/unit7/WarshallReachability"
    },
    {
        id: 5,
        title: "Warshall Algo to Transitive Closure",
        content: "TBD",
        link: "/unit7/WarshallTransitive"
    }
    ]


const Unit7 = () => {

    return (
        <div>
            <h1>
                Section 7.1
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

export default Unit7