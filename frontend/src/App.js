import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Community from './pages/Community';
import AIMentor from './pages/AIMentor';
import Leaderboard from './pages/Leaderboard';
import NotFound from './pages/NotFound';

/**
 * Main application component that handles routing.
 */
const App = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/community" element={<Community />} />
            <Route path="/ai-mentor" element={<AIMentor />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="*" element={<NotFound />} />
        </Routes>
    );
};

export default App;
