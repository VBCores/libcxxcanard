# C++ wrapper for libcanard

## Task interpretation rules

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- Trivial tasks should have trivial solutions

## Change and coding guidance

### Architectural guidelines

- **Minimal code entities**: When implementing features, derive the smallest set of functions, classes, and types that covers all requirements without duplication.
  * Unify equivalent types: if two structs/classes represent the same concept with minor field differences, consolidate into one canonical type.
  * Unify equivalent logic: if the same behavior is needed in 2+ places, extract it - don't inline it twice.
  * Split logic/types into smaller ones if that would reduce total number of entities:
    - feature 1 requires A
    - feature 2 requires B
    - feature 3 requires A+B
    - For this example lets say that semantically, having unified A+B is correct. But that would then require having unified A+B and sub entities A, B in composition. If we forego unification here and for feature 3 use A, B separately (*IF that does not cause code size bloat*), it is preferable because we have 1 less entity
  * Treat this as a set-cover problem: mentally enumerate the sub-operations across all features, then find the minimal set of reusable entities that satisfies them.
- **No redundancy**: if class encapsulates some primitive and wraps some logic for it and is never reused (i.e. only owned by some other class), then this "owner class" should have this primitive and logic, without intermediary; if feature requires adding a field, but this field is never referenced outside of the class, it does not need a getter/setter
- **Fail fast**: if some guarantees that we expect are not met, just crash and print something to cerr; i.e. if we designate/design some argument combination as "impossible" we should fail as a "warning" that impossible happened; if we are in a situation where fallback or fault-recovery would be surprising to user or counter-intuitive, we should just crash. Summary: add checks at trust boundaries, not defensively throughout internal logic

### Practical guidelines

- Do not create small helper methods if they are referenced only once, "inline" them
- Prefer moving self-contained classes / sets of functions into includable .hpp
- Do not split .hpp into header/source before it reaches 300 lines.

### Style and intent

Prefer small, direct changes. Keep everything as simple as reasonable and practical. Avoid "production enterprise ready" mentality. Yes, all code should be complete and correct, but its scope and use case is very clearly defined and bound to this one app, so we do not need to mind any other use cases, other users, etc.

## Testing guidelines

When done editing, always at least smoke all the functionality you *touched* and test all the functionality you *changed*.

## Текст

Рекомендации по написанию текста (от них можно отступать при необходимости):

- Минимизируй пафосные вводные конструкции вроде «в современном мире», «в условиях быстро меняющейся реальности», «на сегодняшний день» и подобные.
- Минимизируй негативный параллелизм и псевдодраму: «не просто…, а…», «это не…, это…»
- Минимизируй рубленые предложения подряд. Текст должен течь естественно.
- Минимизируй использование длинных тире. Используй их только там, где они действительно нужны.
- Минимизируй лишние кавычки. Оставляй кавычки только там, где без них невозможно.
- Минимизируй количество слова «это». Пиши фразы так, чтобы текст звучал естественно.
- Минимизируй искусственные списки вроде «во-первых, во-вторых, в-третьих», если они не нужны.
- Минимизируй канцелярские конструкции: «имеет важное значение»,«позволяет повысить эффективность».
- Минимизируй пустые экспертные фразы: «важно отметить», «следует учитывать», если они не несут смысловой нагрузки
- Минимизируй гиперобобщения: «в современном бизнесе», «в наше время».
- Упрощай избыточные формулировки. Вместо «эффективная стратегия устойчивого роста» пиши просто и понятно.
- Сделай текст живым: добавь разговорную интонацию, естественные переходы и простые формулировки.
- Предпочитай понятные, четкие, минимально-достаточные формулировки вместо длинных, но не экономь за счет фактической точности
