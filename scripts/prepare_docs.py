"""Assemble the repository README files into a temporary Zensical site."""

from pathlib import Path
from collections.abc import Callable
import re
import shutil


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "docs-build"
SPRINT_PATTERN = re.compile(r"^sprint\d{2}-.+")
FEATURE_PATTERN = re.compile(r"^feature\d{2}-.+")


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_assets(source_dir: Path, destination_dir: Path) -> int:
    if not source_dir.is_dir():
        return 0

    copied = 0
    for source in sorted(path for path in source_dir.rglob("*") if path.is_file()):
        copy_file(source, destination_dir / source.relative_to(source_dir))
        copied += 1
    return copied


def is_single_document(source_dir: Path) -> bool:
    return (
        (source_dir / "README.md").is_file()
        and sum(1 for path in source_dir.rglob("*.md") if path.is_file()) == 1
    )


def copy_chapter(
    source_dir: Path,
    destination_dir: Path,
    transform: Callable[[str], str] | None = None,
) -> tuple[int, int]:
    readme = source_dir / "README.md"
    if not readme.is_file():
        return 0, 0

    destination = destination_dir / "index.md"
    if transform is None:
        copy_file(readme, destination)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            transform(readme.read_text(encoding="utf-8")),
            encoding="utf-8",
        )
    assets = copy_assets(source_dir / "assets", destination_dir / "assets")
    return 1, assets


def copy_single_document_feature(
    source_dir: Path, destination_dir: Path
) -> tuple[int, int]:
    readme = source_dir / "README.md"
    destination = destination_dir / f"{source_dir.name}.md"
    asset_prefix = f"assets/{source_dir.name}/"
    content = readme.read_text(encoding="utf-8").replace(
        "./assets/", asset_prefix
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")
    assets = copy_assets(
        source_dir / "assets",
        destination_dir / "assets" / source_dir.name,
    )
    return 1, assets


def main() -> None:
    if not (ROOT / "README.md").is_file():
        raise SystemExit("README.md is required")

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir()

    pages = 0
    assets = 0

    copy_file(ROOT / "README.md", BUILD_DIR / "index.md")
    pages += 1

    for name in ("ROADMAP.md", "CURRENT.md"):
        source = ROOT / name
        if source.is_file():
            copy_file(source, BUILD_DIR / name)
            pages += 1

    for sprint in sorted(ROOT.iterdir()):
        if not sprint.is_dir() or not SPRINT_PATTERN.match(sprint.name):
            continue

        features = [
            feature
            for feature in sorted(sprint.iterdir())
            if feature.is_dir() and FEATURE_PATTERN.match(feature.name)
        ]
        flat_features = {
            feature.name for feature in features if is_single_document(feature)
        }

        def rewrite_sprint_links(content: str) -> str:
            for feature_name in flat_features:
                content = content.replace(
                    f"]({feature_name}/)", f"]({feature_name}.md)"
                )
            return content

        sprint_pages, sprint_assets = copy_chapter(
            sprint, BUILD_DIR / sprint.name, rewrite_sprint_links
        )
        pages += sprint_pages
        assets += sprint_assets

        for feature in features:
            if feature.name in flat_features:
                feature_pages, feature_assets = copy_single_document_feature(
                    feature, BUILD_DIR / sprint.name
                )
            else:
                feature_pages, feature_assets = copy_chapter(
                    feature, BUILD_DIR / sprint.name / feature.name
                )
            pages += feature_pages
            assets += feature_assets

    experiments = ROOT / "experiments"
    if experiments.is_dir():
        for experiment in sorted(experiments.iterdir()):
            if not experiment.is_dir():
                continue
            experiment_pages, experiment_assets = copy_chapter(
                experiment, BUILD_DIR / "experiments" / experiment.name
            )
            pages += experiment_pages
            assets += experiment_assets

    katex = ROOT / "docs" / "javascripts" / "katex.js"
    if katex.is_file():
        copy_file(katex, BUILD_DIR / "javascripts" / katex.name)

    print(f"Prepared {pages} pages and {assets} assets in {BUILD_DIR}")


if __name__ == "__main__":
    main()
