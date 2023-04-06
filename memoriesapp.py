from flask import Flask, jsonify, request
import sqlite3

conn = sqlite3.connect('memories.db')
c = conn.cursor()

# Create memories table
c.execute('''CREATE TABLE IF NOT EXISTS memories
             (id INTEGER PRIMARY KEY, title TEXT, description TEXT)''')

conn.commit()
conn.close()

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

@app.route('/memories', methods=['GET'])
def obter_memo():
    conn = sqlite3.connect('memories.db')
    c = conn.cursor()
    c.execute("SELECT * FROM memories")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/memories/<int:id>', methods=['GET'])
def obter_memo_id(id):
    conn = sqlite3.connect('memories.db')
    c = conn.cursor()
    c.execute("SELECT * FROM memories WHERE id=?", (id,))
    data = c.fetchone()
    conn.close()
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'Memory not found'})

@app.route('/memories/<int:id>' , methods=['PUT'])
def edit_mem_id(id):
    conn = sqlite3.connect('memories.db')
    c = conn.cursor()
    memory_up = request.get_json()
    c.execute("UPDATE memories SET title=?, description=? WHERE id=?", 
              (memory_up['title'], memory_up['description'], id))
    conn.commit()
    c.execute("SELECT * FROM memories WHERE id=?", (id,))
    data = c.fetchone()
    conn.close()
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'Memory not found'})

@app.route('/memories' , methods=['POST'])
def add_memory():
    conn = sqlite3.connect('memories.db')
    c = conn.cursor()
    new_mem = request.get_json()
    c.execute("INSERT INTO memories (title, description) VALUES (?, ?)", 
              (new_mem['title'], new_mem['description']))
    conn.commit()
    c.execute("SELECT * FROM memories WHERE id=?", (c.lastrowid,))
    data = c.fetchone()
    conn.close()
    return jsonify(data)

@app.route('/memories/<int:id>' , methods=['DELETE'])
def delete_mem(id):
    conn = sqlite3.connect('memories.db')
    c = conn.cursor()
    c.execute("DELETE FROM memories WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Memory deleted successfully'})