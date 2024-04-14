import streamlit as st
import os
import openai
import networkx as nx
import matplotlib.pyplot as plt
import random
from PIL import Image
import numpy as np
import tempfile

openai.api_key = "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"  # Replace with your actual API key

def get_edge_labels(t: list):
    dct = {}
    length_of_t = len(t)
    for i in range(length_of_t):
        t[i][0] = t[i][0].replace('"', "").replace("'", "").strip()
        t[i][2] = t[i][2].replace('"', "").replace("'", "").strip()
        t[i][1] = t[i][1].replace('"', "").replace("'", "")
        dct[(t[i][0], t[i][2])] = t[i][1]
    return dct

def knowledge_graph(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates a list of relationships in the format [ENTITY 1, RELATIONSHIP, ENTITY 2] based on a given prompt."},
            {"role": "user", "content": f"Given a prompt, extrapolate as many relationships as possible from it and provide a list of updates.\n\nIf an update is a relationship, provide [ENTITY 1, RELATIONSHIP, ENTITY 2]. The relationship is directed, so the order matters.\n\nIf an update is related to deleting an entity, provide [\"DELETE\", ENTITY].\n\nExample:\nprompt: Alice is Bob's roommate. Alice likes music. Her roommate likes sports\nupdates:\n[[\"Alice\", \"roommate\", \"Bob\"],[\"Alice\",\"likes\",\"music\"],[\"Bob\",\"likes\",\"sports\"]]\n\nprompt: {prompt}\nupdates:"}
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    r = response["choices"][0]["message"]["content"]
    r = r[2:]
    r = r.replace("[", '').replace("]", "")
    r = r.split(",")
    t = []
    for i in range(len(r) // 3):
        t.append(r[3 * i:3 * i + 3])

    G = nx.Graph()
    new_nodes = []
    edge_labels = get_edge_labels(t)

    for i in t:
        if not i[0] in new_nodes:
            new_nodes.append(i[0])
            G.add_node(i[0])
        if not i[2] in new_nodes:
            new_nodes.append(i[2])
            G.add_node(i[2])
        G.add_edge(i[0], i[2])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, labels={node: node for node in G.nodes()})

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=edge_labels,
        font_color='red'
    )

    # Create a temporary file using tempfile.NamedTemporaryFile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
        temp_filename = temp.name

        plt.savefig(temp_filename)
        plt.close('all')  # Close the figure

    img = Image.open(temp_filename)
    image_array = np.asarray(img)

    # Remove the temporary file after image is loaded
    os.remove(temp_filename)

    return image_array

# Streamlit UI
st.title("Knowledge Graph Generator")

# Input prompt from user
prompt = st.text_area("Enter a prompt:")

# Button to generate the graph
if st.button("Generate Graph"):
    # Call the knowledge_graph function and get the image array
    image_array = knowledge_graph(prompt)

    # Display the image
    st.image(image_array, use_column_width=True)
