# 1. Objetivo - criação, visualização, edição e exclusão de memorias relacionadas
     #ao seriado Rick and Morty / create, read, update, delete memories related to
     #Rick and Morty Series

# 2. Endpoints -
    
    # localhost/memories (POST)
    # localhost/memories (GET)
    # localhost/memories/id (GET)
    # localhost/memories/id (PUT)
    # localhost/memories/id (DELETE)

# 3. Recursos - Rick and Morty Memories

from flask import Flask, jsonify, request

app = Flask(__name__)

memories = [

    {
        'id' : 1,
        'memory' : "I had barely sleep, my mind wouldn't stop thinking about Jessica, and then my drunk grandfather entered",
        'S_EP' : 'season 1, episode 1' 
    },
    
   {
        'id' : 2,
        'memory' : "grampa said they were robots, but they have families and they love each other too, I just killed them",
        'S_EP' : 'season 1, episode 1'
    } 
]

# localhost/memories (GET)

@app.route('/memories', methods=['GET'])

def obter_memo():
    return jsonify(memories)

# localhost/memories/id (GET)  

@app.route('/memories/<int:id>', methods=['GET'])
def obter_memo_id(id):
    for memory in memories:
        if memory.get('id') == id:
            return jsonify(memory)
        

# localhost/memories/id (PUT) 

@app.route('/memories/<int:id>' , methods=['PUT'])

def edit_mem_id(id):
    memory_up = request.get_json()
    for indice, memory in enumerate(memories):
        if memory.get('id') == id:
            memories[indice].update(memory_up)
            return jsonify(memories[indice])      
        

# localhost/memories (POST)        

@app.route('/memories' , methods=['POST'])

def add_memory():
    new_mem = request.get_json()
    memories.append(new_mem)
    return jsonify(memories)

# localhost/memories/id (DELETE)
@app.route('/memories/<int:id>' , methods=['DELETE'])

def delete_mem(id):
    for indice, memory in enumerate(memories):
        if memory.get('id') == id:
            del memories[indice]
    return jsonify(memories)        


app.run(port=5000 , host='localhost' , debug=True)


   
