import React from 'react';
import ChatInterface from '../components/ChatInterface';
import { fetchData } from '../utils/api';

/**
 * AI Mentor page component.
 * Displays a chat interface for interacting with the AI mentor.
 */
const AIMentor = () => {
    const [messages, setMessages] = React.useState([]);
    const [input, setInput] = React.useState('');

    const handleSend = async () => {
        const newMessages = [...messages, input];
        setMessages(newMessages);
        setInput('');
        try {
            const response = await fetchData('ai/mentor', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ userId: 'userId', prompt: input }),
            });
            setMessages([...newMessages, response]);
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    return (
        <div className="ai-mentor-page">
            <h1>AI Mentor</h1>
            <ChatInterface messages={messages} inputPlaceholder="Ask a question..." />
            <button onClick={handleSend}>Send</button>
        </div>
    );
};

export default AIMentor;
