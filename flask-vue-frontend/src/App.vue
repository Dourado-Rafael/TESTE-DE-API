<template>
  <div id="app">
    <header>
      <div class="logo-container">
        <img src="IC.png" alt="Logo" class="logo" />
      </div>
    </header>
    <main>
      <input 
        type="text" 
        v-model="termo" 
        placeholder="Digite um termo para buscar..." 
        @keyup.enter="buscar"
      />
      <button @click="buscar">Pesquisar</button>

      <div v-if="loading" class="loading">
        <div class="spinner"></div>
      </div>
      <div v-else>
        <div v-if="resultados.length === 0" class="no-results">Nenhum resultado encontrado.</div>
        <div v-else>
          <h2>Resultados:</h2>
          <ul>
            <li v-for="(resultado, index) in resultados" :key="index">
              <strong>{{ resultado.Razao_Social }}</strong> - {{ resultado.Outra_Coluna }}
            </li>
          </ul>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termo: '', // Termo da pesquisa
      resultados: [], // Resultados da pesquisa
      loading: false, // Indicador de carregamento
    };
  },
  methods: {
    async buscar() {
      if (!this.termo) {
        alert('Por favor, insira um termo para buscar.');
        return;
      }

      this.loading = true;
      try {
        const response = await fetch(`http://127.0.0.1:5000/pesquisar?termo=${encodeURIComponent(this.termo)}`);
        if (!response.ok) {
          throw new Error('Erro na resposta da API');
        }
        const data = await response.json();
        this.resultados = data;
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
        alert('Erro ao buscar dados. Verifique a API.');
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style>
/* Estilo geral */
body {
  margin: 0;
  background-color: #f3eefc; /* Fundo lilás bem suave */
}

#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 20px auto;
  color: #4b3f72; /* Roxo escuro suave */
  background-color: #fff; /* Fundo branco para contraste */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  max-width: 800px;
}

/* Cabeçalho */
header {
  background-color: #7d5ba6; /* Roxo médio sofisticado */
  color: white;
  padding: 20px;
  border-radius: 10px 10px 0 0;
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  height: 40px;
  margin-right: 15px;
}

header h1 {
  margin: 0;
  font-size: 24px;
}

/* Entrada de texto e botão */
input {
  padding: 10px;
  margin-right: 10px;
  width: 300px;
  border: 1px solid #cbb2d6;
  border-radius: 5px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

input:focus {
  border-color: #7d5ba6;
  box-shadow: 0 0 5px rgba(125, 91, 166, 0.4);
  outline: none;
}

button {
  padding: 10px 15px;
  background-color: #7d5ba6;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

button:hover {
  background-color: #6b4d99;
  transform: translateY(-2px);
}

/* Lista de resultados */
ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 10px;
  border: 1px solid #cbb2d6;
  margin: 5px 0;
  border-radius: 5px;
  background-color: #fff;
  transition: transform 0.2s, box-shadow 0.2s;
}

li:hover {
  transform: scale(1.02);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Mensagens de carregamento e sem resultados */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #7d5ba6;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
}

.no-results {
  color: #999;
  margin: 20px 0;
}

h2 {
  color: #7d5ba6;
  margin-bottom: 10px;
}

/* Animações */
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
