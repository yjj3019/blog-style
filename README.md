# 한국어 블로그 글쓰기 스킬

이 저장소는 실제 경험을 바탕으로 한 한국어 블로그 포스팅을 자연스럽게 작성하고 다듬는 공통 Agent Skill을 제공합니다. ChatGPT와 Claude의 Skills 업로드에 쓸 수 있는 ZIP 패키지를 만들 수 있고, Codex·Claude Code·Grok Build에서는 저장소 또는 사용자별 설치 경로에서 사용할 수 있습니다.

휴대폰 화면에서도 읽기 편한 구성을 우선하며, 사실과 개인 경험을 지어내지 않습니다. 공개용 글에서 민감정보와 개인정보를 제외하는 규칙도 포함합니다.

## 저장소 주소만 받은 AI의 동작

AI가 저장소 URL만 받으면 블로그 글쓰기 스킬을 사용하거나 설치하라는 요청으로 처리합니다. `AGENTS.md`와 스킬 원본을 읽고 현재 AI 환경에 맞는 방법을 선택합니다. 설치를 완료했다고 말하기 전에 해당 플랫폼에서 설치되었는지 확인합니다.

## 플랫폼별 사용 방법

### ChatGPT

1. 저장소를 내려받거나 작업 공간에서 엽니다.
2. `python3 scripts/package_skill.py`를 실행합니다.
3. 생성된 `dist/yjj3019-blog-writer.zip`을 ChatGPT의 **Plugins → Skills → Create → Upload from your computer**에서 업로드합니다.

계정, 제품 화면, 작업 공간 설정에 따라 Skills 사용이나 업로드가 제공되지 않을 수 있습니다. Skills의 설치와 동기화 방식도 표면별로 다를 수 있으니, 모바일과 데스크톱에서 각각 목록을 확인하세요. 업로드 기능이 보이지 않으면 해당 대화에 `SKILL.md` 내용을 제공해 현재 대화에서 사용하세요.

### Claude

Claude 웹·데스크톱·모바일 앱에서는 위에서 만든 ZIP을 **Customize → Skills → Create skill → Upload a skill**에서 업로드합니다.

Claude Code에서는 저장소를 프로젝트로 열면 `.claude/skills/yjj3019-blog-writer/SKILL.md`를 읽습니다. 사용자 전체에 설치하려면 다음처럼 실행합니다.

```bash
python3 scripts/install.py --agent claude --scope user
```

Claude Code용 저장소 마켓플레이스 설치:

```text
/plugin marketplace add yjj3019/blog-style
/plugin install yjj3019-blog-style@blog-style
```

### Grok

**Grok Build:** 저장소를 프로젝트 폴더로 열면 `.claude/skills`의 스킬을 자동으로 읽습니다. `grok inspect`로 인식 여부를 확인할 수 있습니다. 사용자별로 설치하려면 다음처럼 실행합니다.

```bash
python3 scripts/install.py --agent grok --scope user
```

Grok Build는 Claude Code의 스킬과 플러그인 형식도 읽으므로 위 Claude Code 마켓플레이스 방식으로 설치한 플러그인도 사용할 수 있습니다.

**Grok Bot:** `SKILL.md`를 첨부하거나 내용을 대화에 붙여 넣은 뒤, “이 지침을 `yjj3019-blog-writer`라는 재사용 스킬로 저장해 줘. 글의 사실과 경험을 지어내지 말고, 개인정보와 민감정보는 저장하거나 공개하지 마.”라고 요청합니다. 저장된 개인 스킬은 Grok Bot의 스킬 목록에서 확인합니다.

일반 Grok 대화에서 저장 가능한 스킬 기능이 보이지 않으면 `SKILL.md`를 첨부하고 현재 대화에 적용해 달라고 요청하세요. 이 경우 영구 저장이 아니라 해당 대화에서만 사용됩니다.

### Codex

Codex에서 저장소를 열면 `.agents/skills/yjj3019-blog-writer/SKILL.md`를 사용할 수 있습니다. 사용자 전체 설치는 다음과 같습니다.

```bash
python3 scripts/install.py --agent codex --scope user
```

Codex 플러그인 마켓플레이스:

```text
codex plugin marketplace add https://github.com/yjj3019/blog-style.git
```

### 로컬 AI 도구에 설치하기

Codex, Claude Code, Grok Build를 각각 설치할 수 있습니다.

```bash
python3 scripts/install.py --agent all --scope user
```

`--agent codex`, `--agent claude`, `--agent grok`으로 한 도구만 지정할 수 있습니다. `--scope project`를 쓰면 현재 저장소에만 설치합니다. Codex와 Grok Build는 사용자별 설치 경로를 공유하므로 스크립트는 같은 파일을 중복 복사하지 않습니다. 설치 스크립트는 스킬 파일만 복사하며 네트워크 요청이나 패키지 설치를 하지 않습니다.

## 포함 파일

- `skills/yjj3019-blog-writer/SKILL.md`: 공통 스킬 원본
- `.agents/skills/yjj3019-blog-writer/SKILL.md`: Codex 및 Grok Build용 프로젝트 사본
- `.claude/skills/yjj3019-blog-writer/SKILL.md`: Claude Code 및 Grok Build용 프로젝트 사본
- `.claude-plugin/`: Claude Code와 Grok Build용 플러그인·마켓플레이스 설정
- `.agents/plugins/marketplace.json` 및 `plugin.json`: Codex 플러그인 패키지 설정
- `scripts/install.py`: Codex, Claude Code, Grok Build용 사용자별 또는 프로젝트별 설치 스크립트
- `scripts/package_skill.py`: ChatGPT와 Claude 앱에서 업로드할 ZIP 생성 스크립트

세 개의 `SKILL.md` 사본은 같은 내용을 유지합니다. 수정할 때 함께 갱신하세요.

## 개인정보 및 민감정보

스킬과 예시에 블로그 글 원문, 사적인 대화, 계정 정보, 비밀 키 또는 민감한 개인 이력을 넣지 않습니다. 완성 글에서도 이름, 연락처, 정확한 거주지, 계정·인증 정보, 금융·건강 정보, 미성년자나 제삼자를 식별할 수 있는 내용을 제외합니다. 제공된 민감한 내용도 공개용 글, 사진 설명, 태그, 코드, 작성 메모에 반복하지 않습니다.

## 공식 문서

- [ChatGPT Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude Skills 업로드](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Grok Build Skills 및 플러그인](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Grok Bot Skills](https://docs.x.ai/grok-bot/skills-routines-and-automations)
