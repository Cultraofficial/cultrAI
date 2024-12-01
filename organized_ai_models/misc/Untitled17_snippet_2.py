# Step 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Set the path where models will be saved
model_save_path = "/content/drive/MyDrive/colab_models/"

# Step 2: Import necessary libraries for downloading models
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Hugging Face Tokens (automatically applied)
huggingface_token_1 = "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"  # First token
huggingface_token_2 = "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"  # Newest token

# List of models to be downloaded (from Hugging Face or alternatives)
model_list = [
    "AdapterHub/modular-task-adaptive",
    "AI-Vision/environmental-analysis",
    "AI2-THOR/3D-environment-simulator",
    "AlphaCode/advanced-coding-model",
    "AntiBiasBERT/FairAI",
    "Artbreeder-AI/visual-style-transfer",
    "AutoML-Zero/auto-model-optimization",
    "BigGAN/high-quality-image-generation",
    "BigScience/BLOOM-176B",
    "BioBERT/biomedical-model",
    "BioGPT/biotech-focused-interactions",
    "Blip-2/visual-language-understanding",
    "CivicGPT/civic-engagement",
    "CLIP/linking-visual-and-text-data",
    "Codex-Cushman/code-generation-backend",
    "Codex-Davinci-2/advanced-code-generation",
    "Cognitive-Model-for-Personal-Memory/avatar-memory",
    "ControlGAN/controlled-image-generation",
    "ControlNet/structured-guidance",
    "CulturalBERT/cross-cultural-knowledge",
    "CurriculumNet/structured-learning-model",
    "CurriculumNet-Advanced/complex-task-learning",
    "DALL-E-3/high-quality-image-generation",
    "DeepLab/semantic-segmentation",
    "DeepLab-Advanced/urban-fashion-segmentation",
    "DeepMind-MuZero/complex-systems-master",
    "DeepMotion/realistic-avatar-animation",
    "DialogPT/open-domain-conversational-model",
    "DreamBooth/creative-visualization",
    "DreamFusion/text-to-3d-model-conversion",
    "EcoNet/climate-analysis-monitoring",
    "EvoNet/iterative-development-for-evolution",
    "ExplainGPT/error-analysis-and-feedback",
    "Explainability-AI/SHAP-LIME-transparency",
    "FaceFormer/facial-animation-from-audio",
    "Fairseq/inclusive-language-diversity",
    "FinBERT/financial-sentiment-analysis",
    "Galois/advanced-encryption-security",
    "Galactica/scientific-creative-knowledge",
    "Gato/multi-modal-agent-interaction",
    "Gato-Advanced/cross-domain-agent-adaptability",
    "GazeGAN/gaze-estimation-for-realistic-eye-contact",
    "Generative-Pre-Trained-Transformer-GPT-J/robust-NLP",
    "GreenEnergyOpt/sustainable-development-energy-optimization",
    "HarmonyAI/cross-cultural-adaptability",
    "InclusiveGPT/language-inclusivity-representation",
    "JusticeGPT/ethical-decision-making-support",
    "KindGPT/empathy-driven-interaction",
    "Knowledge-Graph-AI-Aristo/structured-knowledge-building",
    "Knowledge-Graph-AI-Advanced/deep-interconnected-knowledge",
    "LaMDA/conversational-flow-model",
    "LAVIS/language-audio-visual-integrated-model",
    "LegalBERT/law-related-interactions-content",
    "MetaAI-CICERO/social-intelligence-negotiation",
    "MetaGen/adaptive-knowledge-transfer",
    "MetaRL/reinforcement-learning-for-self-improvement",
    "MidJourney/artistic-image-generation",
    "MoralBERT/ethical-bias-awareness",
    "MuseNet/music-generation-for-soundscapes",
    "mBERT/multilingual-BERT-model",
    "mBART-50/language-model-for-50-languages",
    "NaturalBERT/environmentally-trained-model",
    "NaturalGPT/human-centered-interactions",
    "OpenAI-Codex/coding-backend-support",
    "OpenAI-Jukebox/music-generation-for-customized-sounds",
    "PIFuHD/3D-human-digitization",
    "Perceiver-IO/cross-functional-understanding",
    "Polyglot-Ko-12.8B/language-diversity-training",
    "PropagandaBERT/detecting-biased-language",
    "ReplikaAI/emotionally-adaptive-chatbot",
    "Salesforce-CodeGen/generates-complex-code",
    "Segment-Anything-Model-SAM/object-segmentation",
    "Segment-Anything-Model-SAM-Advanced/advanced-segmentation",
    "SenseMaker/real-time-emotion-processing",
    "Social-CausalBERT/teaches-social-awareness",
    "Social-Connector-AI/connecting-users-with-similar-interests",
    "SpeculativeGPT/generates-future-scenarios",
    "Stable-Diffusion/realistic-image-generation-for-fashion",
    "SRGAN/super-resolution-image-generator",
    "SustainableAI/sustainable-virtual-development",
    "T5-3B/comprehensive-language-tasks",
    "T5-11B/large-scale-language-model",
    "The-Embodied-AI/physical-interaction-in-virtual-spaces",
    "The-Stylist-AI/virtual-fashion-consultations",
    "TrafficSim/road-safety-traffic-simulation",
    "TransferNet/knowledge-transfer",
    "Turing-NLG-17B/large-advanced-NLP",
    "Visual-ChatGPT/text-and-image-understanding",
    "Vision-Transformer-ViT/visual-processing-for-realistic-avatars",
    "VR-Fashion-Model-Generator/digital-fashion-collection-production",
    "Whisper-Large/ASR-for-speech-recognition",
    "Whisper-Medium/ASR-for-multilingual-capabilities",
    "WhisperX/enhanced-ASR-for-noisy-environments",
    "WorldView-AI/global-cultural-analysis",
    "XLNet/advanced-NLP-for-complex-conversations",
    "Yolov5/visual-detection-model",
    "Zero-Shot-Learning-AI/untrained-object-concept-recognition",
]

# Step 3: Function to download models with automatic key application
def download_model(model_name, save_path, token=None):
    try:
        print(f"Downloading {model_name}...")
        model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=token)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)

        # Save to Google Drive
        model.save_pretrained(os.path.join(save_path, model_name))
        tokenizer.save_pretrained(os.path.join(save_path, model_name))
        print(f"{model_name} downloaded and saved to Google Drive.")
    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")

# Step 4: Loop through models and download them using the provided tokens
for model_name in model_list:
    download_model(model_name, model_save_path, huggingface_token_1)
    download_model(model_name, model_save_path, huggingface_token_2)

# All models will be saved to Google Drive under 'colab_models'
