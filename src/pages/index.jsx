// Filename - pages/index.jsx
//Give the copyright statement and user info statement
import React from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";

const Home = () => {
    return (
        <div>
            <h1>Welcome to Discrete Math Solver</h1>
        </div>
);
};

export default Home;

//Ignore this lower stuff, it's me playing around with aesthetics.
/* import * as React from 'react';
import {
    createTheme, ThemeProvider
} from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardHeader from '@mui/material/CardHeader';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
//import StarIcon from '@mui/icons-material/StarBorder';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import GlobalStyles from '@mui/material/GlobalStyles';
import Container from '@mui/material/Container';

function MyButton() {
  return (
    <button>
      I'm a button
    </button>
  );
}

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const sections = [
    {
        title: 'Section 1',
        description: [
            '1.1',
            '\t Statements',
            '\t Symbolic Representations',
            '\t Tautologies',
            '1.2',
            '\t Propositional Logic',
        ],
        buttonText: 'Solve',
        buttonVariant: 'outlined',
    },
    {
        title: 'Section 3',
        description: [
            '3.1',
            'Recursive Definitions',
        ],
        buttonText: 'Solve',
        buttonVariant: 'outlined',
    },
    {
        title: 'Section 4',
        description: [
            '4.1',
            'Sets',
        ],
        buttonText: 'Solve',
        buttonVariant: 'outlined',
    },
];

const defaultTheme = createTheme();

export default function MyApp() {
  return (
      <ThemeProvider theme={defaultTheme}>
      <GlobalStyles styles={{ ul: { margin: 2, padding: 2, listStyle: 'none' } }} />
      <CssBaseline />
          <Typography
          component="h1"
          variant="h2"
          align="center"
          color="text.primary"
          gutterBottom
        >
          CS 214 Discrete Math Solver
        </Typography>
        <Typography variant="h5" align="center" color="text.secondary" component="p">
          [placeholder for a description if we need it]
        </Typography>

      <Container maxWidth="md" component="main" >
        <Grid container spacing={5} alignItems="flex-end" justifyContent={"space-evenly"}>
          {sections.map((section) => (
            // Enterprise card is full width at sm breakpoint
            <Grid
              item
              key={section.title}
              xs={15}
              md={4.9}
            >
              <Card>
                <CardHeader
                  title={section.title}
                  titleTypographyProps={{ align: 'center' }}
                  subheaderTypographyProps={{
                    align: 'center',
                  }}
                  sx={{
                    backgroundColor: (theme) =>
                      theme.palette.mode === 'light'
                        ? theme.palette.grey[200]
                        : theme.palette.grey[700],
                  }}
                />
                <CardContent>
                  <Box
                    sx={{
                      display: 'flex',
                      justifyContent: 'center',
                      alignItems: 'baseline',
                      mb: 2,

                    }}
                  >
                  </Box>
                  <ul>
                    {section.description.map((line) => (
                      <Typography
                        component="li"
                        variant="subtitle1"
                        align="left"
                        key={line}
                      >
                        {line}
                      </Typography>
                    ))}
                  </ul>
                </CardContent>
                <CardActions>
                  <Button fullWidth>
                    {section.buttonText}
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>
      </ThemeProvider>
  );
}
*/