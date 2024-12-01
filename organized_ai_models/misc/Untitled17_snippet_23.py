from transformers import AutoModel, AutoTokenizer
from huggingface_hub import login
import os

# Hugging Face Authentication with the tokens provided
hf_token1 = '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'
hf_token2 = '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'
login(token=hf_token1)

# List of the 98 models to download
model_names = [
    "AdapterHub/modular-task-adaptive",
    "AI-Vision/environmental-analysis",
    "AI2-THOR/3D-environment-simulator",
    "AlphaCode/advanced-coding-model",
    "AntiBiasBERT/FairAI",
    "Artbreeder-AI/visual-style-transfer",
    "AutoML-Zero/auto-model-optimization",
    "BigGAN/high-quality-image-generation",
    "BigScience/BLOOM-176B",
    "BigScience/BLOOM-560m",
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
    "Zero-Shot-Learning-AI/untrained-object-concept-recognition"
]

# Set the directory where models should be saved on Google Drive
drive_directory = "/content/drive/My Drive/colab_models"
os.makedirs(drive_directory, exist_ok=True)

# Download each model and tokenizer
for model_name in model_names:
    try:
        print(f"Downloading {model_name}...")

        # Attempt to download the model with the first token
        model = AutoModel.from_pretrained(model_name, use_auth_token=hf_token1)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token1)

        # Save the model and tokenizer
        model.save_pretrained(f"{drive_directory}/{model_name}")
        tokenizer.save_pretrained(f"{drive_directory}/{model_name}")

        print(f"Successfully downloaded {model_name} and saved it in Google Drive!")
    except Exception as e:
        print(f"Failed to download {model_name} with token {hf_token1}. Trying the second token...")
        try:
            model = AutoModel.from_pretrained(model_name, use_auth_token=hf_token2)
            tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token2)

            # Save the model and tokenizer
            model.save_pretrained(f"{drive_directory}/{model_name}")
            tokenizer.save_pretrained(f"{drive_directory}/{model_name}")

            print(f"Successfully downloaded {model_name} with second token and saved it!")
        except Exception as e2:
            print(f"Failed to download {model_name} with both tokens. Error: {e2}")

print("Download process completed. Please check your Google Drive folder.")
