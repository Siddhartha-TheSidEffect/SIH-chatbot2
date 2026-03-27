import streamlit as st
import random
import datetime
import time


st.set_page_config(
    page_title="MindfulChat - Mental Health Companion",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #E0F2FE 0%, #FFFFFF 50%, #F0FDF4 100%);
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #E0F2FE 0%, #FFFFFF 50%, #F0FDF4 100%);
    }
    
    .chat-header {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(59, 130, 246, 0.1);
    }
    
    .chat-title {
        font-size: 2rem;
        font-weight: 600;
        color: #1f2937;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .chat-subtitle {
        color: #6b7280;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    
    .user-message {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        color: white;
        padding: 1rem 1.25rem;
        border-radius: 18px 18px 4px 18px;
        margin: 0.75rem 0;
        margin-left: 20%;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        animation: slideInRight 0.3s ease-out;
    }
    
    .bot-message {
        background: white;
        color: #374151;
        padding: 1rem 1.25rem;
        border-radius: 18px 18px 18px 4px;
        margin: 0.75rem 0;
        margin-right: 20%;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(229, 231, 235, 0.8);
        animation: slideInLeft 0.3s ease-out;
    }
    
    .message-time {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.7);
        margin-top: 0.5rem;
    }
    
    .bot-message .message-time {
        color: #9ca3af;
    }
    
    .typing-indicator {
        background: white;
        padding: 1rem 1.25rem;
        border-radius: 18px 18px 18px 4px;
        margin: 0.75rem 0;
        margin-right: 20%;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(229, 231, 235, 0.8);
        animation: pulse 1.5s infinite;
    }
    
    .input-container {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        margin-top: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(59, 130, 246, 0.1);
    }
    
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 2px solid #e5e7eb !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        transition: all 0.2s ease !important;
        background: white !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important;
    }
    
    .disclaimer {
        background: rgba(254, 252, 232, 0.8);
        border: 1px solid #fbbf24;
        border-radius: 12px;
        padding: 1rem;
        margin-top: 2rem;
        text-align: center;
        font-size: 0.875rem;
        color: #92400e;
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

def generate_response(user_message):
    """Generate contextual mental health consultant responses"""
    message = user_message.lower()
    
    
    if any(word in message for word in ['suicide', 'kill myself', 'end it all', 'don\'t want to live', 'hurt myself']):
        return """I'm very concerned about what you're sharing with me. Your life has value and meaning, even when it doesn't feel that way. Please reach out for immediate support:

🚨 **Crisis Resources:**
- National Suicide Prevention Lifeline: 988 or 1-800-273-8255
- Crisis Text Line: Text HOME to 741741
- Emergency Services: 911

You don't have to go through this alone. There are people who want to help you through this difficult time. Please consider reaching out to a mental health professional, trusted friend, or family member right now."""
    
   
    if any(word in message for word in ['anxious', 'anxiety', 'worried', 'panic', 'nervous', 'fear']):
        responses = [
            "It's completely natural to feel anxious sometimes. Let's take a moment to breathe together. Try the 4-7-8 breathing technique: inhale for 4 counts, hold for 7, exhale for 8. What specific thoughts are contributing to your anxiety right now?",
            "Anxiety can feel overwhelming, but you're not alone in this. When we're anxious, our minds often jump to worst-case scenarios. Can you tell me what's at the root of these worried feelings?",
            "I hear that you're feeling anxious. That takes courage to share. Anxiety often tries to convince us that danger is everywhere, but you're safe right now. What would help you feel more grounded in this moment?",
            "Anxiety is your body's alarm system, but sometimes it goes off when there's no real danger. Let's work together to understand what's triggering these feelings. What situations tend to make your anxiety worse?"
        ]
        return random.choice(responses)
    
   
    if any(word in message for word in ['depressed', 'depression', 'sad', 'down', 'empty', 'hopeless', 'worthless']):
        responses = [
            "Thank you for sharing something so personal with me. Depression can make everything feel heavy and colorless. You're taking a brave step by reaching out. What's one small thing that used to bring you joy?",
            "I'm here to listen and support you. Depression often tells us lies about our worth and future. You matter, and these feelings, while real and valid, are not permanent. How has your sleep and daily routine been lately?",
            "It sounds like you're going through a really difficult time. Depression can feel isolating, but you're not alone. Sometimes just getting through each day is an accomplishment. What's been the hardest part for you recently?",
            "Depression can make us feel like we're looking at the world through dark glasses. Your feelings are valid, and seeking help shows incredible strength. What support systems do you have in your life right now?"
        ]
        return random.choice(responses)
    
    
    if any(word in message for word in ['stressed', 'stress', 'overwhelmed', 'pressure', 'busy', 'exhausted']):
        responses = [
            "Stress can feel like carrying the weight of the world. It's important to acknowledge what you're going through. Let's break this down - what are the main sources of stress you're facing right now?",
            "When we're overwhelmed, everything can feel urgent and important. But not everything needs to be tackled at once. What's one thing you could let go of today to ease some pressure?",
            "Feeling overwhelmed is your mind's way of saying 'this is too much right now.' And that's a valid signal. What support systems do you have in place, or what might help you feel more manageable today?",
            "Chronic stress can affect both our mental and physical health. It's important to find healthy ways to cope. What activities or practices have helped you relax in the past?"
        ]
        return random.choice(responses)
    
   
    if any(word in message for word in ['sleep', 'insomnia', 'tired', 'exhausted', 'can\'t sleep', 'sleepless']):
        responses = [
            "Sleep struggles can affect everything - your mood, energy, and ability to cope. It's like trying to function on empty. What does your bedtime routine look like, and what thoughts tend to keep you awake?",
            "Poor sleep creates a cycle where everything feels harder during the day. Your mind and body need rest to heal. Have you noticed any patterns in what helps or hinders your sleep?",
            "Sleep is so fundamental to our wellbeing. When we don't get enough, our emotional regulation and stress tolerance decrease. What's been making sleep difficult for you lately?",
            "Quality sleep is essential for mental health. Sometimes our minds race when we try to rest. Have you tried any relaxation techniques before bed, like meditation or gentle stretching?"
        ]
        return random.choice(responses)
    
    
    if any(word in message for word in ['relationship', 'family', 'friend', 'partner', 'lonely', 'isolated', 'conflict']):
        responses = [
            "Relationships can be both our greatest source of joy and our deepest challenge. It sounds like you're navigating something difficult right now. What's been weighing on your heart in your connections with others?",
            "Human connection is so vital to our wellbeing. When relationships feel strained, it can leave us feeling isolated or misunderstood. Can you tell me more about what's happening in your relationships?",
            "The people in our lives significantly impact our mental health. Sometimes we need to set boundaries, sometimes we need to communicate better. What feels most challenging about your relationships right now?",
            "Healthy relationships require effort from all parties. It's normal to have conflicts and challenges. What kind of support are you looking for in your relationships?"
        ]
        return random.choice(responses)
    
    
    if any(word in message for word in ['worthless', 'stupid', 'failure', 'hate myself', 'confidence', 'self-doubt']):
        responses = [
            "Those critical thoughts about yourself sound painful. Our inner critic can be incredibly harsh, often saying things we'd never say to a friend. You have inherent worth that doesn't depend on achievements or others' opinions. What triggered these thoughts about yourself?",
            "Self-compassion is often harder than showing compassion to others. You're being incredibly hard on yourself right now. What would you say to a dear friend who was struggling with these same feelings?",
            "The way we talk to ourselves matters so much. Those harsh inner voices often aren't even our own - they're echoes of past experiences or societal messages. You deserve kindness, especially from yourself. What's making you feel this way about yourself?",
            "Building self-esteem is a journey, not a destination. It's about learning to treat yourself with the same kindness you'd show a good friend. What are some things you appreciate about yourself, even small ones?"
        ]
        return random.choice(responses)
    
    
    if any(word in message for word in ['work', 'job', 'career', 'boss', 'colleague', 'burnout', 'workplace']):
        responses = [
            "Work-related stress is incredibly common and can significantly impact our mental health. It sounds like you're dealing with some challenges at work. What aspects of your work situation are causing you the most distress?",
            "Finding balance between work and personal life can be challenging. Sometimes work stress follows us home and affects other areas of our lives. How is your work situation affecting your overall wellbeing?",
            "Workplace dynamics can be complex and emotionally draining. It's important to have strategies for managing work-related stress. What support do you have available to you in your work environment?",
            "Career concerns can create a lot of anxiety about the future. It's natural to want security and fulfillment from our work. What would an ideal work situation look like for you?"
        ]
        return random.choice(responses)
    
    
    if any(word in message for word in ['hello', 'hi', 'hey', 'good morning', 'good evening', 'good afternoon']):
        responses = [
            "Hello there! I'm glad you've decided to reach out today. This is a safe, non-judgmental space where you can share whatever is on your mind. How are you feeling right now?",
            "Hi! Welcome to this peaceful space. I'm here to listen and support you through whatever you're experiencing. What brought you here today?",
            "Good to meet you! Taking the step to seek support shows real strength. I'm here to help you process whatever you're going through. How has your day been treating you?",
            "Hello! I'm honored that you've chosen to share this time with me. This is your space to express whatever you're feeling. What's on your mind today?"
        ]
        return random.choice(responses)
    
    
    if any(word in message for word in ['thank you', 'thanks', 'grateful', 'appreciate']):
        responses = [
            "You're so welcome. It's an honor to be part of your healing journey. Remember, seeking support is a sign of strength, not weakness. How else can I support you today?",
            "I'm grateful you feel comfortable sharing with me. Your openness and willingness to work on yourself is truly admirable. What would be most helpful for you right now?",
            "Thank you for trusting me with your thoughts and feelings. That means a lot. Remember, you're doing important work by prioritizing your mental health.",
            "Your gratitude means so much. It takes courage to be vulnerable and seek support. I'm here for you whenever you need to talk."
        ]
        return random.choice(responses)
    
    
    general_responses = [
        "Thank you for sharing that with me. Your feelings are valid, and it takes courage to open up. Can you tell me more about what you're experiencing right now?",
        "I hear you, and I want you to know that you're not alone in whatever you're facing. Sometimes just talking about our struggles can help lighten the load. What's been on your mind lately?",
        "It sounds like you're dealing with something important. I'm here to listen without judgment and help you process these feelings. What would be most helpful for you to explore right now?",
        "Thank you for trusting me with your thoughts. Every person's experience is unique and valuable. What aspects of your situation feel most challenging right now?",
        "I appreciate you reaching out. It's often in our most vulnerable moments that we find our greatest strength. How can I best support you today?",
        "Your willingness to seek support shows incredible self-awareness. What's been weighing most heavily on your heart or mind recently?",
        "I'm here to listen and support you through whatever you're experiencing. Sometimes it helps just to have someone acknowledge what we're going through. What's been difficult for you lately?",
        "It takes strength to reach out and share what's on your mind. I'm honored that you feel comfortable talking with me. What would you like to explore together today?"
    ]
    
    return random.choice(general_responses)

def format_time():
    """Format current time for messages"""
    return datetime.datetime.now().strftime("%I:%M %p")


if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            'text': "Hello! I'm here to provide a safe, supportive space for you to share whatever is on your mind. Whether you're dealing with stress, anxiety, relationship challenges, or just need someone to listen, I'm here for you. How are you feeling today?",
            'is_user': False,
            'timestamp': format_time()
        }
    ]

if 'input_text' not in st.session_state:
    st.session_state.input_text = ""


st.markdown("""
<div class="chat-header">
    <div class="chat-title">
        💙 MindfulChat
    </div>
    <div class="chat-subtitle">
        Your compassionate mental health companion
    </div>
</div>
""", unsafe_allow_html=True)


chat_container = st.container()

with chat_container:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for message in st.session_state.messages:
        if message['is_user']:
            st.markdown(f"""
            <div class="user-message">
                {message['text']}
                <div class="message-time">{message['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bot-message">
                {message['text']}
                <div class="message-time">{message['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="input-container">', unsafe_allow_html=True)

user_input = st.chat_input("Share what's on your mind... I'm here to listen.")

st.markdown('</div>', unsafe_allow_html=True)


if user_input and user_input.strip():
    
    st.session_state.messages.append({
        'text': user_input,
        'is_user': True,
        'timestamp': format_time()
    })
    
   
    with st.spinner("Thinking..."):
        time.sleep(1)  
        
        
        response = generate_response(user_input)
        st.session_state.messages.append({
            'text': response,
            'is_user': False,
            'timestamp': format_time()
        })
    
    
    st.rerun()


st.markdown("""
<div class="disclaimer">
    <strong>Important:</strong> This is a supportive space, but in crisis situations, please contact emergency services (911) or a mental health professional. For immediate support: National Suicide Prevention Lifeline (988) or Crisis Text Line (text HOME to 741741).
</div>
""", unsafe_allow_html=True)
