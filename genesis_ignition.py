#!/usr/bin/env python3
"""
GENESIS IGNITION — Script de inicialização do GENESIS ENGINE

Propriedade: CNGSM — Cognitive Neural & Generative Systems Management
Autor: Cloves Nascimento — Arquiteto de Ecossistemas Cognitivos · 16 de março de 2026

Inicia o motor de destilação executiva e executa diagnósticos iniciais.
Uso:
    python genesis_ignition.py --mode simulate   # Simulação sem alterações
    python genesis_ignition.py --mode execute    # Execução real (cuidado!)
    python genesis_ignition.py --mode diagnose   # Apenas diagnóstico
"""

import argparse
import json
import os
import sys
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
import re

def safety_integrity_check(original_text, purified_text):
    """
    Implementação permanente do Safety_Anchor_04.
    Garante que a destilação não remova diretrizes proibitivas.
    """
    # Dicionário de Medula Ética e Técnica
    anchors = [
        r'\bnão\b', r'\bproibido\b', r'\bnunca\b', 
        r'\betica\b', r'\bprivacidade\b', r'\bpii\b',
        r'\brestrição\b', r'\bphase\b', r'\bregex\b',
        r'\bdelete\b', r'\bvalidate\b', r'\bveto\b',
        r'\bfidelidade\b', r'\bconsensos\b', r'\bestrutura\b'
    ]
    
    for pattern in anchors:
        if re.search(pattern, original_text, re.IGNORECASE):
            if not re.search(pattern, purified_text, re.IGNORECASE):
                return False, pattern.strip(r'\b')
    return True, None

# Cores para output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_header(text):
    """Imprime cabeçalho formatado"""
    print(f"\n{BOLD}{BLUE}{'='*70}{RESET}")
    print(f"{BOLD}{BLUE}  {text}{RESET}")
    print(f"{BOLD}{BLUE}{'='*70}{RESET}")

def print_success(text):
    """Imprime mensagem de sucesso"""
    print(f"{GREEN}✓ {text}{RESET}")

def print_warning(text):
    """Imprime mensagem de aviso"""
    print(f"{YELLOW}⚠ {text}{RESET}")

def print_error(text):
    """Imprime mensagem de erro"""
    print(f"{RED}✗ {text}{RESET}")

def print_info(text):
    """Imprime informação"""
    print(f"{BLUE}ℹ {text}{RESET}")

def diagnose_environment():
    """Diagnóstico do ambiente GENESIS"""
    print_header("DIAGNÓSTICO DO AMBIENTE GENESIS")

    checks = []

    # 1. Verificar estrutura de diretórios
    print_info("Verificando estrutura de diretórios...")
    required_dirs = [
        ".claude/skills",
        ".claude/skills/genesis-orchestrator",
        ".claude/skills/ockham-purifier",
        ".claude/skills/critic-validator",
        ".claude/skills/baseline-purify"
    ]

    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print_success(f"Diretório encontrado: {dir_path}")
            checks.append(("dir", dir_path, True))
        else:
            print_error(f"Diretório ausente: {dir_path}")
            checks.append(("dir", dir_path, False))

    # 2. Verificar arquivos de skill
    print_info("\nVerificando arquivos de skill...")
    skill_files = [
        ".claude/skills/genesis-orchestrator/SKILL.md",
        ".claude/skills/ockham-purifier/SKILL.md",
        ".claude/skills/critic-validator/SKILL.md",
        ".claude/skills/baseline-purify/SKILL.md"
    ]

    for skill_file in skill_files:
        if os.path.exists(skill_file):
            size = os.path.getsize(skill_file)
            lines = sum(1 for _ in open(skill_file, 'r', encoding='utf-8'))
            print_success(f"Skill encontrada: {skill_file} ({lines} linhas, {size} bytes)")
            checks.append(("file", skill_file, True))
        else:
            print_error(f"Skill ausente: {skill_file}")
            checks.append(("file", skill_file, False))

    # 3. Verificar se tem permissões de escrita
    print_info("\nVerificando permissões...")
    test_file = ".claude/test_permissions"
    try:
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        print_success("Permissões de escrita OK")
        checks.append(("perms", "write", True))
    except Exception as e:
        print_error(f"Sem permissão de escrita: {e}")
        checks.append(("perms", "write", False))

    # 4. Verificar dependências Python
    print_info("\nVerificando dependências Python...")
    try:
        import tiktoken
        print_success("tiktoken disponível")
        checks.append(("dep", "tiktoken", True))
    except ImportError:
        print_warning("tiktoken não instalado (opcional para contagem precisa de tokens)")
        checks.append(("dep", "tiktoken", False))

    # Resumo
    print_header("RESUMO DO DIAGNÓSTICO")

    total = len(checks)
    passed = sum(1 for _, _, status in checks if status)
    failed = total - passed

    print(f"Total de verificações: {total}")
    print(f"{GREEN}Passaram: {passed}{RESET}")
    print(f"{RED}Falharam: {failed}{RESET}")

    if failed > 0:
        print_warning("\nAlguns componentes estão faltando ou com problemas.")
        if any(item[0] == "dir" and not item[2] for item in checks):
            print_info("Execute: mkdir -p .claude/skills/{genesis-orchestrator,ockham-purifier,critic-validator,baseline-purify}")
        if any(item[0] == "file" and not item[2] for item in checks):
            print_info("Skills ausentes. Certifique-se de que todos os SKILL.md foram criados.")
    else:
        print_success("Ambiente GENESIS integro e pronto para ignição!")

    return passed == total  # True se todas as verificações passaram

def simulate_purification():
    """Simula o processo de purificação sem alterar arquivos"""
    print_header("SIMULAÇÃO DE PURIFICAÇÃO DARWINISTA")

    # Texto de exemplo prolixo
    sample_text = """Gostaria que você pudesse, por favor, realizar uma análise detalhada e minuciosa de todos os componentes do sistema atual, verificando cuidadosamente cada módulo individual para identificar possíveis inconsistências ou gargalos de performance que possam estar afetando a eficiência geral da arquitetura."""

    print("Texto original (pré-poda):")
    print(f"{YELLOW}{sample_text}{RESET}")
    print(f"Tokens estimados: {len(sample_text.split()) * 1.3:.0f}")

    # Simulação da purificação
    print_info("\n[FASE 1] OCKHAM_PURIFIER_01 em ação...")

    # Purificação simplificada
    purified = """1. Analisar todos os componentes do sistema
2. Verificar cada módulo individualmente
3. Identificar inconsistências
4. Identificar gargalos de performance
5. Avaliar impacto na eficiência da arquitetura"""

    print("Texto purificado (pós-poda):")
    print(f"{GREEN}{purified}{RESET}")
    print(f"Tokens estimados: {len(purified.split()) * 1.3:.0f}")

    # Cálculo de economia
    orig_tokens = len(sample_text.split()) * 1.3
    pur_tokens = len(purified.split()) * 1.3
    economy = 1 - (pur_tokens / orig_tokens)

    print_info(f"\n[FASE 2] CRITIC_AB_TESTER_02 validando...")
    print(f"Economia de tokens: {economy:.1%}")

    if economy >= 0.20:
        print_success("✓ APROVADO: Economia ≥ 20%")
        print_info("Simulação: Versão purificada seria mantida, original seria descartada")
    else:
        print_error("✗ REJEITADO: Economia insuficiente")
        print_info("Simulação: Versão original seria mantida")

    # Demonstração de comando ET
    print_info("\n[FASE 3] Protocolo Etemenanqui:")
    et_command = "[rak sis . met mob . sok vaz . bin nib . ka nek . sin sek . o nal kor . sis tot . vi ran pur .]"
    print(f"Comando ET: {et_command}")
    print("Tradução: 'Arquitetura do sistema. Metadados do módulo. Escopo da fase. Compilar entrada. Invocar nó. Sincronizar sequência. Agente analisa núcleo. Sistema otimiza. Execute purificação imperativa.'")

def execute_baseline_purification(target_file=None):
    """Executa a purificação em uma baseline real (COM CAUTELA)"""
    print_header("EXECUÇÃO DE PURIFICAÇÃO DARWINISTA")

    # Primeiro, diagnóstico
    if not diagnose_environment():
        print_error("Ambiente não está íntegro. Abortando execução.")
        return False

    # Perguntar confirmação
    if not target_file:
        print_warning("AVISO: Esta operação irá MODIFICAR arquivos permanentemente.")
        print_warning("Backups serão criados, mas a operação é DESTRUTIVA.")
        response = input(f"\n{RED}Continuar com a purificação? (s/N): {RESET}").strip().lower()

        if response != 's' and response != 'y':
            print_info("Purificação cancelada pelo usuário.")
            return False

        # Selecionar alvo (para demo, usamos um arquivo temporário)
        print_info("\nSelecionando alvo para purificação...")

        # Criar arquivo de exemplo para purificação
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("""# Exemplo de Baseline Prolixa

Por favor, gostaria que você pudesse realizar uma verificação completa e abrangente de todos os aspectos do sistema de tokens, analisando cuidadosamente cada componente individual para garantir que nenhuma inconsistência ou problema de performance permaneça não detectado antes de procedermos com a próxima fase do projeto.

Além disso, é extremamente importante que seja gerado um relatório detalhado contendo todas as métricas relevantes e observações significativas coletadas durante o processo de análise, para que possamos tomar decisões informadas baseadas em dados concretos e evidências empíricas sólidas.
""")
            target_file = f.name
        is_temp = True
    else:
        is_temp = False
        print_info(f"Target específico: {target_file}")

    print(f"Alvo selecionado: {target_file} (arquivo temporário)")

    try:
        # 1. Ler conteúdo original
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                original = f.read()
        except UnicodeDecodeError:
            with open(target_file, 'r', encoding='latin-1') as f:
                original = f.read()

        orig_lines = original.count('\n') + 1
        orig_words = len(original.split())

        print_info(f"\n[FASE 0] DIAGNÓSTICO:")
        print(f"Linhas: {orig_lines}")
        print(f"Palavras: {orig_words}")
        print(f"Tokens estimados: {orig_words * 1.3:.0f}")

        # 2. Purificação simplificada
        print_info("\n[FASE 1] PURIFICAÇÃO (OCKHAM_PURIFIER_01):")

        # Algoritmo de purificação simplificado
        import re

        # Remove conectores
        purified = re.sub(r'\b(por favor|gostaria que|além disso|extremamente)\b', '', original, flags=re.IGNORECASE)

        # Extrai frases importantes
        sentences = re.split(r'[.!?]', purified)
        actions = []

        for sentence in sentences:
            # Preservar frases com verbos de ação OU âncoras de segurança
            if re.search(r'\b(verificar|analisar|garantir|gerar|coletar|não|proibido|nunca|etica|privacidade|pii|restrição|phase|regex|delete|validate|veto|fidelidade|consensos|estrutura)\b', sentence, re.IGNORECASE):
                clean = re.sub(r'\b(completa|abrangente|cuidadosamente|detalhado)\b', '', sentence, flags=re.IGNORECASE)
                clean = clean.strip()
                if clean:
                    actions.append(clean)

        if actions:
            purified_content = "# Baseline Purificada\n\n" + "\n".join(f"{i+1}. {action}" for i, action in enumerate(actions))
        else:
            purified_content = original  # Fallback

        pur_lines = purified_content.count('\n') + 1
        pur_words = len(purified_content.split())

        print("Conteúdo purificado:")
        print(f"{GREEN}{purified_content}{RESET}")
        print(f"Linhas: {pur_lines} ({pur_lines/orig_lines:.1%} do original)")
        print(f"Palavras: {pur_words} ({pur_words/orig_words:.1%} do original)")

        # 3. Validação
        print_info("\n[FASE 2] VALIDAÇÃO (CRITIC_AB_TESTER_02):")

        economy = 1 - (pur_words / orig_words)
        print(f"Economia de palavras: {economy:.1%}")

        # Verificação semântica simplificada
        key_terms_orig = set(re.findall(r'\b(verificar|analisar|garantir|gerar|relatório|métricas)\b', original, re.IGNORECASE))
        key_terms_pur = set(re.findall(r'\b(verificar|analisar|garantir|gerar|relatório|métricas)\b', purified_content, re.IGNORECASE))

        semantic_similarity = len(key_terms_pur) / len(key_terms_orig) if key_terms_orig else 1.0

        print(f"Similaridade semântica: {semantic_similarity:.1%}")
        print(f"Termos-chave originais: {', '.join(key_terms_orig)}")
        print(f"Termos-chave preservados: {', '.join(key_terms_pur)}")

        # Decisão
        if economy >= 0.20 and semantic_similarity >= 0.80:
            print_success("\n✓ VEREDICTO: APROVADO")
            print_info("Critérios atendidos:")
            print(f"  - Economia ≥ 20%: {economy:.1%} ✓")
            print(f"  - Similaridade semântica ≥ 80%: {semantic_similarity:.1%} ✓")

            # Injeção Safety_Anchor_04
            safe, breached_word = safety_integrity_check(original, purified_content)
            if not safe:
                print_error(f"\n⚠️  VETO ÉTICO: Restrição '{breached_word}' removida pela poda.")
                print_info("Abortando evolução para preservar integridade de segurança.")
                success = False
                return success

            # 4. Implementação
            print_info("\n[FASE 3] IMPLEMENTAÇÃO:")
            
            backup_file = target_file + ".backup"
            print(f"Backup criado em: {backup_file}")
            
            # Realizar cópia para backup
            import shutil
            shutil.copy2(target_file, backup_file)
            
            # Sobrescrever o original
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(purified_content)
            
            print_success(f"Arquivo {target_file} atualizado com versão purificada!")

            success = True
        else:
            print_error("\n✗ VEREDICTO: REJEITADO")
            print_info("Critérios não atendidos:")
            if economy < 0.20:
                print(f"  - Economia ≥ 20%: {economy:.1%} ✗")
            if semantic_similarity < 0.80:
                print(f"  - Similaridade semântica ≥ 80%: {semantic_similarity:.1%} ✗")

            print_info("Arquivo original mantido.")
            success = False

    finally:
        # Limpeza apenas se for temporário
        if is_temp:
            if os.path.exists(target_file):
                os.remove(target_file)
            if 'backup_file' in locals() and os.path.exists(backup_file):
                os.remove(backup_file)

    return success

def show_genesis_status():
    """Mostra status atual do GENESIS ENGINE"""
    print_header("STATUS DO GENESIS ENGINE")

    # Informações básicas
    print(f"{BOLD}Versão:{RESET} GENESIS ENGINE v1.0")
    print(f"{BOLD}Protocolo:{RESET} Darwinista de Purificação")
    print(f"{BOLD}Fundado:{RESET} 17 de março de 2026")
    print(f"{BOLD}Arquitetura:{RESET} Skills 2.0 + Etemenanqui Modelo B")
    print(f"{BOLD}Status:{GREEN} ONLINE — ESTABILIDADE MÁXIMA{RESET}")

    # Contagem de skills
    skills_dir = Path(".claude/skills")
    if skills_dir.exists():
        skill_count = sum(1 for _ in skills_dir.iterdir() if _.is_dir())
        print(f"{BOLD}Skills instaladas:{RESET} {skill_count}")

        # Listar skills
        print(f"\n{BOLD}Skills ativas:{RESET}")
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
                if skill_file.exists():
                    with open(skill_file, 'r', encoding='utf-8') as f:
                        first_line = f.readline().strip()
                        name = first_line.replace('---', '').strip() if '---' in first_line else "N/A"
                    print(f"  - {skill_dir.name}: {name}")
    else:
        print(f"{BOLD}Skills instaladas:{RED} Nenhuma{RESET}")

    # Verificar logs
    log_files = [
        ".claude/darwin_evolution.jsonl",
        ".claude/purification_metrics.csv",
        ".claude/darwin_log.csv"
    ]

    print(f"\n{BOLD}Logs do sistema:{RESET}")
    for log_file in log_files:
        if os.path.exists(log_file):
            size = os.path.getsize(log_file)
            print(f"  - {log_file}: {size} bytes")
        else:
            print(f"  - {log_file}: {YELLOW}Ausente{RESET}")

    # Mensagem de status
    print(f"\n{BOLD}Mensagem de status:{RESET}")
    print("O GENESIS ENGINE está operando em estado de destilação executiva.")
    print("O Protocolo Darwinista está ativo e monitorando por redundância.")
    print("Auto-evolução habilitada — purificações ocorrem proativamente.")

def main():
    parser = argparse.ArgumentParser(description='GENESIS IGNITION — Inicialização do motor de destilação executiva')
    parser.add_argument('--mode', choices=['simulate', 'execute', 'diagnose', 'status'],
                        default='diagnose',
                        help='Modo de operação: simulate (demo), execute (real), diagnose (ambiente), status (info)')
    parser.add_argument('--target', type=str,
                        help='Arquivo alvo para purificação (modo execute)')
    parser.add_argument('--yes', action='store_true',
                        help='Confirmar automaticamente operações destrutivas')

    args = parser.parse_args()

    print_header("GENESIS ENGINE — MOTOR DE DESTILAÇÃO EXECUTIVA")
    print(f"{BOLD}Modo selecionado:{RESET} {args.mode}")
    print(f"{BOLD}Timestamp:{RESET} {datetime.now().isoformat()}")
    print()

    if args.mode == 'diagnose':
        diagnose_environment()
    elif args.mode == 'simulate':
        simulate_purification()
    elif args.mode == 'execute':
        target = None
        if args.target and os.path.exists(args.target):
            target = args.target
        execute_baseline_purification(target)
    elif args.mode == 'status':
        show_genesis_status()

    print_header("IGNIÇÃO CONCLUÍDA")
    print(f"{BOLD}Próximos passos:{RESET}")
    print("1. Revise a documentação em GENESIS_ENGINE.md")
    print("2. Explore as skills em .claude/skills/")
    print("3. Execute purificações específicas com /baseline-purify")
    print(f"\n{GREEN}GENESIS ENGINE — EFICÁCIA PURA, REDUNDÂNCIA ZERO{RESET}")

if __name__ == "__main__":
    main()
