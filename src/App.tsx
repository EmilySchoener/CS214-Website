import React from "react";
import Navbar from "./Navbar/index.jsx";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";

//These are the webpages available.
import Home from './pages/index.jsx';
import About from './pages/about.jsx';
import Unit1 from "./pages/unit1.jsx";
import Section1_1 from "./pages/section1.jsx";
import Section1_2 from "./pages/section1_2.jsx";
import Section1_either from "./pages/section1_either.jsx";
import Unit3 from "./pages/unit3.jsx";
import Chap3 from "./pages/chap3.jsx";
import Unit4 from "./pages/unit4.jsx";
import TrueOrFalse from "./pages/4_1pages/TrueOrFalse.jsx";
import PowerSet from "./pages/4_1pages/PowerSet.jsx";
import BinaryOrUnary from "./pages/4_1pages/BinaryOrUnary.jsx";
import SolveExpression from "./pages/4_1pages/SolveExpression.jsx";
import Unit5 from "./pages/unit5.jsx";
import Section5_1 from "./pages/section5_1.jsx";
import BinaryRelations from "./pages/5_1pages/BinaryRelations.jsx";
import ClosureRelations from "./pages/5_1pages/ClosureRelations.jsx";
import HasseDiagram from "./pages/5_1pages/HasseDiagram.jsx";
import MMLGElements from "./pages/5_1pages/MMLGElements.jsx";
import Equivalence from "./pages/5_1pages/Equivalence.jsx";
import Section5_2 from "./pages/section5_2.jsx";
import PertChart from "./pages/5_2pages/PertChart.jsx";
import TopologicalSort from "./pages/5_2pages/TopologicalSort.jsx";
import SequentialTasks from "./pages/5_2pages/SequentialTasks.jsx";
import Section5_4 from "./pages/section5_4.jsx";
import CyclicalPermutations from "./pages/5_4pages/CyclicalPermutations.jsx";
import Onto from "./pages/5_4pages/Onto.jsx";
import OneToOne from "./pages/5_4pages/OneToOne.jsx";
import CompositionofCycles from "./pages/5_4pages/CompositionofCycles.jsx";
import Section5_5 from "./pages/section5_5.jsx";
import OrderOfMagnitude from "./pages/5_5pages/OrderOfMagnitude.jsx";
import MasterTheorem from "./pages/5_5pages/MasterTheorem.jsx";
import Section5_7 from "./pages/section5_7.jsx";
import BooleanMatrices from "./pages/5_7pages/BooleanMatrices.jsx";
import MatrixMultiplication from "./pages/5_7pages/MatrixMultiplication.jsx";
import Unit6 from "./pages/unit6.jsx";
import Section6_1 from "./pages/section6_1.jsx";
import Section6_2 from "./pages/section6_2.jsx";
import Unit7 from "./pages/unit7.jsx";
import Report from "./pages/ErrorReport.jsx";


//Router is for different paths on the navbar. Home is the homepage.
function App() {
    return (
        <div>
            <Router>
                <Navbar/>
                <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route path="/about" element={<About/>}/>
                    <Route path="/unit1" element={<Unit1/>}/>
                    <Route path="/unit1/section1_1" element={<Section1_1/>}/>
                    <Route path="/unit1/section1_either" element={<Section1_either/>}/>
                    <Route path="/unit1/section1_2" element={<Section1_2/>}/>
                    <Route path="/unit3" element={<Chap3/>}/>
                    <Route path="/unit3/recursiveDef" element={<Unit3/>}/>
                    <Route path="/unit4" element={<Unit4/>}/>
                    <Route path="/unit4/TrueOrFalse" element={<TrueOrFalse/>}/>
                    <Route path="/unit4/PowerSet" element={<PowerSet/>}/>
                    <Route path="/unit4/BinaryOrUnary" element={<BinaryOrUnary/>}/>
                    <Route path="/unit4/SolveExpression" element={<SolveExpression/>}/>
                    <Route path="/unit5" element={<Unit5/>}/>
                    <Route path="/unit5/section5_1" element={<Section5_1/>}/>
                    <Route path="/unit5/section5_1/BinaryRelations" element={<BinaryRelations/>}/>
                    <Route path="/unit5/section5_1/ClosureRelations" element={<ClosureRelations/>}/>
                    <Route path="/unit5/section5_1/HasseDiagram" element={<HasseDiagram/>}/>
                    <Route path="/unit5/section5_1/MMLGElements" element={<MMLGElements/>}/>
                    <Route path="/unit5/section5_1/Equivalence" element={<Equivalence/>}/>
                    <Route path="/unit5/section5_2" element={<Section5_2/>}/>
                    <Route path="/unit5/section5_2/PertChart" element={<PertChart/>}/>
                    <Route path="/unit5/section5_2/TopologicalSort" element={<TopologicalSort/>}/>
                    <Route path="/unit5/section5_2/SequentialTasks" element={<SequentialTasks/>}/>
                    <Route path="/unit5/section5_4" element={<Section5_4/>}/>
                    <Route path="/unit5/section5_4/CyclicalPermutations" element={<CyclicalPermutations/>}/>
                    <Route path="/unit5/section5_4/Onto" element={<Onto/>}/>
                    <Route path="/unit5/section5_4/OneToOne" element={<OneToOne/>}/>
                    <Route path="/unit5/section5_4/CompositionofCycles" element={<CompositionofCycles/>}/>
                    <Route path="/unit5/section5_5" element={<Section5_5/>}/>
                    <Route path="/unit5/section5_5/OrderOfMagnitude" element={<OrderOfMagnitude/>}/>
                    <Route path="/unit5/section5_5/MasterTheorem" element={<MasterTheorem/>}/>
                    <Route path="/unit5/section5_7" element={<Section5_7/>}/>
                    <Route path="/unit5/section5_7/BooleanMatrices" element={<BooleanMatrices/>}/>
                    <Route path="/unit5/section5_7/MatrixMultiplication" element={<MatrixMultiplication/>}/>
                    <Route path="/unit6" element={<Unit6/>}/>
                    <Route path="/unit6/section6_1" element={<Section6_1/>}/>
                    <Route path="/unit6/section6_2" element={<Section6_2/>}/>
                    <Route path="/unit7" element={<Unit7/>}/>
                    <Route path="/userReport" element={<Report/>}/>
                </Routes>
                <br/>
                <a href={"/userReport"}>
                    <button> Report an Error </button>
                </a>
                <p>Examples taken from: Mathematical Structures for Computer Science, A Modern Treatment of Discrete
                    Mathematics (7th edition) by Judith L. Gerstring</p>
            </Router>
        </div>
    );
}

export default App;
