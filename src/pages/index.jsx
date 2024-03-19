// Filename - pages/index.jsx
//Give the copyright statement and user info statement
import * as React from 'react';
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

const units = [
    {
        id: 1,
        title: "Unit 1",
        content: [{id: 1, name:"1.1 Statements, Symbolic Representations and Tautologies"},
            {id: 2, name:"1.2 Propositional Logic"}],
        link: "/unit1"
    },
    {
        id: 2,
        title: "Unit 3",
        content: [{id:1, name:"3.1 Recursive Definitions"}],
        link: "/unit3"
    },
    {
        id: 3,
        title: "Unit 4",
        content: [{id:1, name:"4.1 Sets"}],
        link: "/unit4"
    },
    {
        id: 4,
        title: "Unit 5",
        content: [{id: 1, name:"5.1 Relations"},
        {id: 2, name:"5.2 Topological Sorting"},
        {id: 3, name:"5.4 Functions"},
        {id: 4, name:"5.5 Order of Magnitude"},
        {id: 5, name:"5.7 Boolean Matrices"}],
        link: "/unit5"
    },
    {
        id: 5,
        title: "Unit 6",
        content: [{id: 1, name:"6.1 Graphs and Their Representations"},
        {id: 2, name:"6.2 Trees and Their Representations"}],
        link: "/unit6"
    },
    {
        id: 6,
        title: "Unit 7",
        content: [{id: 1, name:"7.1 Directed Graphs and Binary Relations; Washall's Algorithm"}],
        link: "/unit7"
    }
]


const Home = () => {
return (
    <>
        <h1>Welcome to Discrete Math Solver</h1>
        <span style ={{ fontSize: 20}}>
        <p>All examples from this website are taken from the current UAH CS214 textbook:
            <br/>
            <span style={{fontStyle:'italic'}}>Mathematical Structures for Computer Science, A Modern Treatment of Discrete Mathematics </span>
                (7th edition) by Judith L. Gerstring.
        </p></span>
        <h2>Units</h2>
        <Box sx={{flexGrow: 1}} >
            <Grid container spacing={1} columns={{xs: 2, sm: 10, md: 15}}>
                {units.map((unit, index) => (
                    <Grid item xs={2} sm={4} md={4} key={index}>
                        <Item>
                            <Card>
                                <h2>{unit.title}</h2>
                                <ListGroup>
                                    {
                                        unit.content.map(item => (
                                            <ListGroup.Item className="modal-bg" key={item.id}>
                                                <span style={{fontSize: 14, fontWeight: 'bold'}}>{item.name} </span>
                                            </ListGroup.Item>
                                        ))
                                    }
                                </ListGroup>
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
    </>
);

};
export default Home;

