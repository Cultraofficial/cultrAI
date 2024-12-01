content_data = {
    "title": "Interactive Movie Scene 1",
    "description": "The first scene of the interactive movie.",
    "options": [
        {"text": "Go left", "next_scene_id": "scene_2_left"},
        {"text": "Go right", "next_scene_id": "scene_2_right"}
    ]
}
add_document("Content", content_data, document_id="scene_1")
