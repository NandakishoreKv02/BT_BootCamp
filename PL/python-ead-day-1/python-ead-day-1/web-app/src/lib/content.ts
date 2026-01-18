import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

// Path to content directory (parent of web-app)
const contentDirectory = path.join(process.cwd(), '..', 'content');

export interface Frontmatter {
  title: string;
  type: string;
  module: string;
  unit: string;
  order?: number;
  difficulty?: string;
  tags?: string[] | { topics?: string[]; subtopics?: string[] };
  use_case?: string;
  domain?: string;
  lab_number?: number;
  duration_hours?: number;
  subtopics?: Array<{ name: string; exercises: number[] }>;
}

export interface ContentItem {
  slug: string;
  frontmatter: Frontmatter;
  content: string;
}

/**
 * Get all modules from the content directory
 */
export function getAllModules(): string[] {
  const modulesPath = path.join(contentDirectory, 'modules');
  if (!fs.existsSync(modulesPath)) {
    return [];
  }
  return fs.readdirSync(modulesPath).filter((file) => {
    return fs.statSync(path.join(modulesPath, file)).isDirectory();
  });
}

/**
 * Get all units for a specific module
 */
export function getUnitsForModule(moduleName: string): string[] {
  const modulePath = path.join(contentDirectory, 'modules', moduleName);
  if (!fs.existsSync(modulePath)) {
    return [];
  }
  const units = fs.readdirSync(modulePath).filter((file) => {
    const filePath = path.join(modulePath, file);
    return fs.statSync(filePath).isDirectory() && file.startsWith('unit_');
  });

  // Sort units numerically by extracting both module and unit numbers
  // Handles patterns like: unit_1_3, unit_2_10, unit_3_1, unit_4_2, etc.
  return units.sort((a, b) => {
    const aMatch = a.match(/unit_(\d+)_(\d+)/);
    const bMatch = b.match(/unit_(\d+)_(\d+)/);

    if (!aMatch || !bMatch) return 0;

    const aModuleNum = parseInt(aMatch[1], 10);
    const bModuleNum = parseInt(bMatch[1], 10);
    const aUnitNum = parseInt(aMatch[2], 10);
    const bUnitNum = parseInt(bMatch[2], 10);

    // Sort by module number first, then by unit number
    if (aModuleNum !== bModuleNum) {
      return aModuleNum - bModuleNum;
    }
    return aUnitNum - bUnitNum;
  });
}

/**
 * Get knowledge content for a specific unit
 */
export function getKnowledgeContent(
  moduleName: string,
  unitName: string
): ContentItem | null {
  const knowledgePath = path.join(
    contentDirectory,
    'modules',
    moduleName,
    unitName,
    'knowledge'
  );

  if (!fs.existsSync(knowledgePath)) {
    return null;
  }

  const files = fs.readdirSync(knowledgePath);
  const mdFile = files.find((file) => file.endsWith('.md'));

  if (!mdFile) {
    return null;
  }

  const fullPath = path.join(knowledgePath, mdFile);
  const fileContents = fs.readFileSync(fullPath, 'utf8');
  const { data, content } = matter(fileContents);

  return {
    slug: mdFile.replace(/\.md$/, ''),
    frontmatter: data as Frontmatter,
    content,
  };
}

/**
 * Get exercises README for a specific unit
 */
export function getExercisesContent(
  moduleName: string,
  unitName: string
): ContentItem | null {
  const exercisesPath = path.join(
    contentDirectory,
    'modules',
    moduleName,
    unitName,
    'exercises',
    'README.md'
  );

  if (!fs.existsSync(exercisesPath)) {
    return null;
  }

  const fileContents = fs.readFileSync(exercisesPath, 'utf8');
  const { data, content } = matter(fileContents);

  return {
    slug: 'exercises',
    frontmatter: data as Frontmatter,
    content,
  };
}

/**
 * Get all app labs for a specific unit
 */
export function getAppLabsForUnit(
  moduleName: string,
  unitName: string
): ContentItem[] {
  const labsPath = path.join(
    contentDirectory,
    'modules',
    moduleName,
    unitName,
    'app_labs'
  );

  if (!fs.existsSync(labsPath)) {
    return [];
  }

  const labs: ContentItem[] = [];
  const labFolders = fs.readdirSync(labsPath).filter((file) => {
    return fs.statSync(path.join(labsPath, file)).isDirectory();
  });

  for (const labFolder of labFolders) {
    const readmePath = path.join(labsPath, labFolder, 'README.md');
    if (fs.existsSync(readmePath)) {
      const fileContents = fs.readFileSync(readmePath, 'utf8');
      const { data, content } = matter(fileContents);

      labs.push({
        slug: labFolder,
        frontmatter: data as Frontmatter,
        content,
      });
    }
  }

  return labs.sort((a, b) => (a.frontmatter.order || 0) - (b.frontmatter.order || 0));
}

/**
 * Get learning outcomes for a specific unit
 */
export function getLearningOutcomes(
  moduleName: string,
  unitName: string
): ContentItem | null {
  const outcomesPath = path.join(
    contentDirectory,
    'modules',
    moduleName,
    unitName,
    'LEARNING_OUTCOMES.md'
  );

  if (!fs.existsSync(outcomesPath)) {
    return null;
  }

  const fileContents = fs.readFileSync(outcomesPath, 'utf8');
  const { data, content } = matter(fileContents);

  return {
    slug: 'learning-outcomes',
    frontmatter: data as Frontmatter,
    content,
  };
}
