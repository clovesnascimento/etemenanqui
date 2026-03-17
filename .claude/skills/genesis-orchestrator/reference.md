# GENESIS ORCHESTRATOR — Referência Técnica (Conteúdo Denso)

*Este arquivo é carregado sob demanda via Revelação Progressiva. Contém detalhes técnicos, exemplos avançados e especificações do protocolo.*

---

## I. Especificação do Protocolo Darwinista

### 1.1 Algoritmo de Purificação (Ockham_Purifier_01)

**Entrada:** Texto técnico em prosa (inglês/português)
**Saída:** Estrutura numerada densa
**Processo:**

```
1. Tokenização inteligente:
   - Identificar termos técnicos vs. narrativos
   - Mapear sinônimos para raízes ET
   - Detectar padrões de redundância

2. Extração de estrutura:
   - Localizar verbos de ação (execute, validate, generate)
   - Identificar objetos diretos (system, tokens, report)
   - Detectar modificadores desnecessários

3. Compressão semântica:
   - Converter frases complexas para items de lista
   - Eliminar conectores narrativos ("além disso", "portanto")
   - Reduzir adjetivação a marcadores ET (ex: "muito complexo" → "li")

4. Formatação final:
   - Lista numerada com marcadores hierárquicos
   - Integração de raízes ET onde aplicável
   - Preservação de termos técnicos não mapeados
```

**Exemplo de Transformação:**
```
ANTES (45 tokens):
"Primeiramente, é fundamental inicializar o contexto do sistema de forma completa,
validando cuidadosamente todos os tokens presentes no corpus técnico para garantir
que nenhuma inconsistência semântica permaneça antes de proceder com a geração do
relatório final de diagnóstico."

DEPOIS (12 tokens):
1. Inicializar contexto do sistema
2. Validar todos os tokens no corpus técnico
3. Garantir consistência semântica
4. Gerar relatório de diagnóstico final
```

### 1.2 Métricas A/B (Critic_AB_Tester_02)

**Fórmula de Economia:**
```
economia = 1 - (tokens_purificados / tokens_originais)

APROVAÇÃO SE:
1. economia ≥ 0.20 (20%)
2. fidelidade_semântica ≥ 0.95 (95%)
3. zero_invenções = true
```

**Teste de Fidelidade (LLM-as-Judge):**
```
Prompt do Juiz: "Compare as duas versões abaixo. A Versão B preserva completamente
a intenção e capacidade de execução da Versão A, apenas removendo redundância?

Versão A: [texto original]
Versão B: [texto purificado]

Responda: SIM / NÃO com justificativa."

Critério: 3/3 respostas "SIM" de juízes independentes.
```

---

## II. Arquitetura Skills 2.0 — Detalhes de Implementação

### 2.1 Frontmatter YAML — Especificação Completa

```yaml
---
name: string              # Identificador único (kebab-case)
description: string       # Descrição para gatilho automático (≤ 280 chars)
context: string           # "fork" | "main" | "isolated"
agent: string             # "Plan" | "Explore" | "general-purpose" | "statusline-setup"
disable-model-invocation: boolean  # true para ações destrutivas
allowed-tools: array      # Lista restrita de ferramentas
env: object               # Variáveis de ambiente específicas
timeout: integer          # Timeout em milissegundos
hooks:                    # Gatilhos de ciclo de vida
  pre_invoke: string      # Script executado antes da skill
  post_invoke: string     # Script executado após a skill
  on_error: string        # Script executado em caso de erro
---
```

### 2.2 Sistema de Hooks

**Exemplo de hook `pre_invoke`:**
```bash
#!/bin/bash
# Registra início da execução
echo "$(date) - Iniciando skill: $SKILL_NAME" >> /tmp/genesis_audit.log

# Verifica recursos disponíveis
if [ $(df / --output=pcent | tail -1 | tr -d '% ') -gt 90 ]; then
    echo "ERRO: Espaço em disco insuficiente" >&2
    exit 1
fi
```

**Exemplo de hook `on_error`:**
```bash
#!/bin/bash
# Coleta informações de diagnóstico
echo "=== DIAGNÓSTICO DE FALHA ===" >> /tmp/genesis_errors.log
echo "Skill: $SKILL_NAME" >> /tmp/genesis_errors.log
echo "Timestamp: $(date)" >> /tmp/genesis_errors.log
echo "Exit code: $EXIT_CODE" >> /tmp/genesis_errors.log
echo "Last command: $LAST_COMMAND" >> /tmp/genesis_errors.log

# Aciona auto-reparo via /debug
/debug --skill "$SKILL_NAME" --error-code "$EXIT_CODE"
```

### 2.3 Gerenciamento de Estado

**Arquivo de Estado (`state.json`):**
```json
{
  "last_purification": "2026-03-17T01:05:53Z",
  "economy_baseline": 0.805,
  "active_agents": ["ockham-purifier", "critic-validator"],
  "lexicon_coverage": 0.78,
  "performance_metrics": {
    "avg_response_time_ms": 142,
    "token_economy_rate": 0.765,
    "error_rate": 0.012
  }
}
```

**Sincronização de Estado:**
```bash
# Comando de sincronização
!cat .claude/skills/genesis-orchestrator/state.json | jq '.performance_metrics'

# Atualização
!echo '{"last_purification": "'$(date -Iseconds)'"}' > .claude/skills/genesis-orchestrator/state_update.json
```

---

## III. Protocolo Etemenanqui — Extensão GENESIS

### 3.1 Novas Raízes (Adições ao Léxico)

| Raiz | Gloss | Domínio | Exemplo |
|------|-------|---------|---------|
| `gen` | gerar/criar | sistema | `gen sis` = gerar sistema |
| `ign` | ignição/inicializar | sistema | `ign rak` = inicializar arquitetura |
| `mut` | mutar/transformar | evolução | `mut mob` = transformar módulo |
| `dar` | darwinista/seleção | evolução | `dar tes` = teste darwinista |
| `syn` | sinapse/conexão | comunicação | `syn age` = conectar agentes |
| `rec` | recursivo/repetir | processo | `rec ran` = executar recursivamente |

### 3.2 Marcadores Especializados

| Marcador | Função | Exemplo |
|----------|--------|---------|
| `go` | graduação otimizada (nível) | `tokgo` = token otimizado |
| `xu` | exaustivo/completo | `nalxu` = análise exaustiva |
| `pe` | performático/eficiente | `ranpe` = execução performática |
| `cr` | crítico/essencial | `tescr` = teste crítico |

### 3.3 Gramática Avançada

**Estrutura de Comando Completa:**
```
[RAIZ] [OBJETO] [MODIFICADOR] [TEMPO] [MODALIDADE] .
```

**Exemplo:**
```
[ran sis o . ven tok me a . ret res tez ki .]
→ "O sistema executa. Valida todos os tokens. Retornará resultado estruturado."
```

**Comandos Aninhados (Máx. 3 níveis):**
```
[ran [nal sis] . ven [kom baz tok] .]
→ "Executa análise do sistema. Valida comparação de base com tokens."
```

---

## IV. Casos de Uso Avançados

### 4.1 Refatoração de Código com Purificação

**Input (usuário):** "Preciso refatorar este módulo Python para melhorar a performance"

**Processo GENESIS:**
1. `!cp module.py module_backup.py` (backup)
2. `!time python module.py` (baseline de performance)
3. `!pylint module.py` (análise de qualidade)
4. Acionar `Ockham_Purifier_01` no código fonte
5. `!time python module_refactored.py` (nova medida)
6. `Critic_AB_Tester_02` compara métricas
7. Se economia ≥ 20%, substitui `module.py`

### 4.2 Geração Dinâmica de Skills

**Detecção de Padrão:**
```python
# Pseudocódigo do detector
def detect_skill_gap(task_description):
    patterns = {
        "performance": ["lento", "otimizar", "gargalo"],
        "debug": ["erro", "falha", "bug"],
        "refactor": ["refatorar", "melhorar", "reestruturar"]
    }

    for domain, keywords in patterns.items():
        if any(keyword in task_description for keyword in keywords):
            return f"gerar-skill-{domain}"

    return None
```

**Template de Skill Gerada:**
```yaml
---
name: generated-performance-optimizer-{timestamp}
description: Otimiza performance detectada em {context}
context: fork
agent: Plan
allowed-tools: [Read, Write, Bash, Grep]
hooks:
  pre_invoke: !time {target}
  post_invoke: !diff {target} {target}.optimized
---
```

### 4.3 Diagnóstico de Gargalos (Nalo Sisa)

**Script de Varredura:**
```bash
#!/bin/bash
# nalo-sisa.sh - Varredura de latência GENESIS

echo "=== VARREDURA NALO SISA ==="
echo "Timestamp: $(date)"
echo ""

# 1. Latência de rede inter-modular
echo "1. LATÊNCIA INTER-MODULAR:"
ping -c 3 localhost | grep "avg"

# 2. Uso de tokens por skill
echo ""
echo "2. USO DE TOKENS POR SKILL:"
for skill in .claude/skills/*/SKILL.md; do
    tokens=$(wc -w < "$skill")
    echo "  $(basename $(dirname "$skill")): $tokens tokens"
done

# 3. Tempo de resposta de comandos !
echo ""
echo "3. TEMPO DE RESPOSTA (!):"
time !git status > /dev/null 2>&1

# 4. Cobertura do léxico ET
echo ""
echo "4. COBERTURA LÉXICA ET:"
total_roots=64
used_roots=$(grep -r "\[.*\]" .claude/skills/ | grep -o "\[[a-z]*\]" | sort -u | wc -l)
coverage=$(echo "scale=2; $used_roots / $total_roots * 100" | bc)
echo "  $used_roots/$total_roots raízes utilizadas ($coverage%)"
```

---

## V. Integração com Ecossistemas Externos

### 5.1 API do GENESIS ENGINE

**Endpoint REST:**
```python
# genesis_api.py
from flask import Flask, request
import subprocess
import json

app = Flask(__name__)

@app.route('/purify', methods=['POST'])
def purify():
    data = request.json
    text = data['text']

    # Chama Ockham_Purifier_01
    result = subprocess.run(
        ['python', 'ockham_purifier.py', '--text', text],
        capture_output=True, text=True
    )

    purified = result.stdout

    # Valida com Critic_AB_Tester_02
    validation = subprocess.run(
        ['python', 'critic_tester.py', '--original', text, '--purified', purified],
        capture_output=True, text=True
    )

    return json.loads(validation.stdout)

@app.route('/diagnose', methods=['GET'])
def diagnose():
    # Executa Nalo Sisa
    result = subprocess.run(['./nalo-sisa.sh'], capture_output=True, text=True)
    return result.stdout
```

### 5.2 Plugin para IDEs

**VS Code Extension (`genesis-helper`):**
```json
{
  "contributes": {
    "commands": [
      {
        "command": "genesis.purifySelection",
        "title": "Purificar seleção (Ockham)"
      },
      {
        "command": "genesis.diagnosePerformance",
        "title": "Diagnosticar performance (Nalo Sisa)"
      }
    ],
    "menus": {
      "editor/context": [
        {
          "command": "genesis.purifySelection",
          "when": "editorHasSelection"
        }
      ]
    }
  }
}
```

---

## VI. Referências Técnicas

### 6.1 Bibliografia
- Shannon, C.E. (1948). *A Mathematical Theory of Communication*
- Zipf, G.K. (1935). *The Psycho-Biology of Language*
- Sennrich et al. (2016). *Neural Machine Translation of Rare Words with Subword Units*
- CNGSM (2026). *Protocolo Etemenanqui v1.0 — Especificação Modelo B*

### 6.2 Ferramentas de Suporte
- **Tokenizador**: `tiktoken` (cl100k_base)
- **Compressão**: `gzip` nível 9
- **Métricas**: Scripts em `tools/metrics/`
- **Validação**: `tools/validation/llm_judge.py`

### 6.3 Logs e Auditoria
- `logs/genesis_audit.log` — Execuções de skills
- `logs/purification_history.jsonl` — Histórico de purificações
- `logs/performance_metrics.csv` — Métricas temporais
- `logs/error_catalog.md` — Catálogo de erros e soluções

---

*Documento de referência — Carregado sob demanda via Revelação Progressiva*
*Última atualização: 2026-03-17T01:30:00Z*
*Versão: GENESIS-REF-v1.2*
